import frappe
from frappe.utils.background_jobs import enqueue
from frappe import msgprint, _
import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def get_context(context):
    user = frappe.get_doc("User", frappe.session.user)  
    hash_str = get_random_string(8)
    context.access = True
    context.user = frappe.session.user
    # if user.name == "Guest" or not frappe.db.exists("Session OTP Users", {"verified":1, "user":user.name,"phone_no":user.mobile_no}):
    if user.name == "Guest" :
        context.access = False
        return context
    customer = frappe.get_doc("Customer", {"mobile_no": user.mobile_no, })
    contact = frappe.get_doc("Contact", customer.customer_primary_contact)
    for row in contact.email_ids:
        if not row.custom_is_verified:
            context.email_verified = row.email_id
    
    email_args = {
				"recipients": [context.email_verified],
				"template": "verification_mail",
				"subject": 'Email Verification',
        "args":dict(
        user=user.name,
        hash_str=hash_str,
    ),}

    context.time_remaining = 0
    email_sent_creation  = frappe.db.sql(f"""
    SELECT max(creation) as creation, user_id
    FROM `tabEmails Sent`
    where user_id = "{frappe.session.user}"
    """, as_dict=1)
    if email_sent_creation and email_sent_creation[0]["creation"]:
      from frappe.utils import now, pretty_date
      import datetime

      time_change = datetime.timedelta(minutes=3, seconds=10) 
      if email_sent_creation[0]["creation"] + time_change < datetime.datetime.now():
        enqueue(method=frappe.sendmail, queue='short', timeout=10,**email_args)
      else:
        context.time_remaining = datetime.datetime.now() - (email_sent_creation[0]["creation"] + time_change)
    else:
        doc = frappe.new_doc('Emails Sent')
        doc.user_id = user.name
        doc.insert()
        frappe.db.commit()
        enqueue(method=frappe.sendmail, queue='short', timeout=10,**email_args)