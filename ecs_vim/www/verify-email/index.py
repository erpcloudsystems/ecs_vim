import frappe
from frappe.utils.background_jobs import enqueue
from frappe import msgprint, _

def get_context(context):
    pass

@frappe.whitelist(allow_guest=True)
def verify_email():
    user = frappe.session.user
    contact = frappe.get_doc("Contact", {"user":user})
    verification_status = {}
    for row in contact.email_ids:
        row.custom_is_verified = 1
    contact.save()
    return True
    