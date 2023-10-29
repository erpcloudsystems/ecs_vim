import frappe


def get_context(context):
    user = frappe.get_doc("User", frappe.session.user)  
    context.access = True
    # if user.name == "Guest" or not frappe.db.exists("Session OTP Users", {"verified":1, "user":user.name,"phone_no":user.mobile_no}):
    if user.name == "Guest" :
        context.access = False
        return context
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
