import frappe

from ecs_vim.api import create_customer_or_supplier
from frappe.rate_limiter import rate_limit

def get_context(context):
    user = frappe.get_doc("User", frappe.session.user)  
    context.access = True
    # if user.name == "Guest" or not frappe.db.exists("Session OTP Users", {"verified":1, "user":user.name,"phone_no":user.mobile_no}):
    if user.name == "Guest" :
        context.access = False
        return context
    create_customer_or_supplier()
    prepare_input_values(context, user)


def prepare_input_values(context, user):
    customer = frappe.get_doc("Customer", {"mobile_no": user.mobile_no, "custom_user":user.name})
    # no he have customer and user docs
    # initialize DOM inputs
    context.first_name = user.first_name or ""
    context.last_name  = user.last_name or ""
    context.email  = user.email or ""
    context.mobile_no  = user.mobile_no or ""
    context.custom_finished_details  = customer.custom_finished_details

    
@frappe.whitelist(allow_guest=True)
@rate_limit(limit=20000, seconds=24 * 60 * 60)
def verify_account():

    user = frappe.session.user
    contact = frappe.get_doc("Contact", {"user":user})
    verification_status = {}
    for row in contact.email_ids:
        verification_status["email"] = row.email_id
        verification_status["email_verified"] = row.custom_is_verified
    
    for row in contact.phone_nos:
        verification_status["mobile_no"] = row.phone
        verification_status["mobile_no_verified"] = row.custom_is_verified

    return verification_status

@frappe.whitelist(allow_guest=True)
@rate_limit(limit=20000, seconds=24 * 60 * 60)
def finished_details():

    user = frappe.session.user
    if user != "Guest":

        customer = frappe.get_doc("Customer", {"custom_user":user})
        customer.custom_finished_details = 1
        customer.flags.ignore_mandatory = True
        customer.save(ignore_permissions=True)

@frappe.whitelist(allow_guest=True)
def checked_finished_details():
    user = frappe.session.user
    if user != "Guest":
        customer = frappe.get_doc("Customer", {"custom_user":user})
        if customer.custom_finished_details == 1:
            return "/customer-details"
        return False
    