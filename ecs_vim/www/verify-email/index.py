import frappe
from frappe.utils.background_jobs import enqueue
from frappe import msgprint, _

def get_context(context):
    user = frappe.session.user
    if not frappe.db.exists("Emails Sent", {"hash_str":frappe.form_dict.hash_str}):
        context.response = "Not Found"
    else:
        import datetime
        import pytz
        email_sent = frappe.get_doc("Emails Sent", {"hash_str":frappe.form_dict.hash_str})
        time_change = datetime.timedelta(minutes=60, seconds=10) 
        if (pytz.timezone("Asia/Riyadh").localize(email_sent.creation)  + time_change) < datetime.datetime.now(tz=pytz.timezone("Asia/Riyadh")):
            context.response = "Activation Link Expired"
        elif email_sent.verified:
            context.response = "Already Activated Successfully"
        else:
            contact = frappe.get_doc("Contact", {"user":user})
            for row in contact.email_ids:
                if row.email_id == frappe.session.user:
                    row.custom_is_verified = 1
            email_sent.verified = 1
            contact.save(ignore_permissions=True)
            email_sent.save(ignore_permissions=True)
            frappe.db.commit()
            context.response = "Activated Successfully"


    