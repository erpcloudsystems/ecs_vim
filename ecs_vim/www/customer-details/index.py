import frappe
from frappe.utils import today, add_to_date
from frappe.utils.background_jobs import enqueue


def verify_account():

    user = frappe.session.user
    contact = frappe.get_doc("Contact", {"user":user})
    verification_status = {}
    verification_status["email"] = False
    verification_status["email_verified"] = False
    for row in contact.email_ids:
      if row.email_id == frappe.session.user:
        verification_status["email"] = row.email_id
        verification_status["email_verified"] = row.custom_is_verified
    
    for row in contact.phone_nos:
        verification_status["mobile_no"] = row.phone
        verification_status["mobile_no_verified"] = row.custom_is_verified

    return verification_status

def get_context(context):
    user = frappe.get_doc("User", frappe.session.user)  
    context.access = True
    # if user.name == "Guest" or not frappe.db.exists("Session OTP Users", {"verified":1, "user":user.name,"phone_no":user.mobile_no}):
    if user.name == "Guest" :
        context.access = False
        return context
    
    prepare_input_values(context, user)


def prepare_input_values(context, user):
    customer = frappe.get_doc("Customer", {"mobile_no": user.mobile_no})
    # no he have customer and user docs
    # initialize DOM inputs
    context.first_name = user.first_name or ""
    context.last_name  = user.last_name or ""
    context.email  = user.email or ""
    context.username  = user.username or ""
    context.mobile_no  = user.mobile_no or ""
    context.custom_finished_details  = customer.custom_finished_details
    context.user_image  = user.user_image
    adults_count = 0
    childrens_count = 0
    for row in customer.customer_family_detail:
        if row.adult :
            adults_count +=1
        else:
            if row.child:
                childrens_count +=1 

    context.adults_count  = adults_count
    context.childrens_count  = childrens_count
    context.customer_family_detail = customer.customer_family_detail

    contact = frappe.get_doc("Contact", customer.customer_primary_contact)
    context.coupon_code = False
    for row in contact.email_ids:
        if not row.custom_is_verified:
            context.email_verified = row.email_id
    create_coupon_code(customer.custom_first_login, customer, context)

def send_mail(name):

    email_args = {
        "recipients": [frappe.session.user],
        "template": "send_coupon",
				"subject": 'Email Verification',
         "args":dict(
        coupon_code=name,
        user=frappe.session.user,
    ),
        }
    enqueue(method=frappe.sendmail, queue='short', **email_args)
def create_coupon_code(custom_first_login, customer, context):
    context.custom_first_login = 0
    context.verified_customer = 0
    r = verify_account()
    if r["email_verified"] and r["mobile_no_verified"]:
        context.verified_customer = 1
        customer.save(ignore_permissions=True)
        if not frappe.db.exists("Coupon Code", customer.name):
            context.custom_first_login = 1
            coupon_code = frappe.get_doc({
                "doctype": "Coupon Code",
                "custom_customer": customer.name,
                "coupon_name":customer.name,
                "coupon_code": "VIM" + frappe.generate_hash(length=5),
                "pricing_rule": "50 Riyal Discount",
                "valid_from":today(),
                "valid_upto":add_to_date(today(), years=3, as_string=True),
                "maximum_use":1,
                "description":customer.mobile_no

            })
            coupon_code.insert(ignore_permissions=True)
            context.coupon_code = coupon_code.coupon_code
            frappe.db.commit()
            send_mail(coupon_code.coupon_code)
    context.list_of_coupons = frappe.db.get_all("Coupon Code", {"custom_customer":customer.name}, ["coupon_code", "pricing_rule", "maximum_use", "used"])