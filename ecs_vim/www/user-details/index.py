# import frappe
# from ecs_vim.ecs_vim.api import create_customer_or_supplier
# def get_context(context):
#     from frappe.contacts.doctype.contact.contact import get_contact_name
#     import string
#     import random
#     user = frappe.session.user
#     ignore_links=False 
#     ignore_mandatory=False    
#     # initializing size of string
#     N = 7
    
#     # using random.choices()
#     # generating random strings
#     res = ''.join(random.choices(string.ascii_uppercase +
#                                 string.digits, k=N))
#     if user.name in ["Administrator", "Guest"]:
#         return
#     try:
#         create_customer_or_supplier()
#     except:
#         doc = frappe.get_doc({
#             'doctype': 'Task',
#             'title': res
#         })
#         doc.insert()
#     mobile_no = frappe.db.get_value("User", {"email_id": user.email_id}, "mobile_no")
#     # mobile_contact_name = frappe.db.get_value("Contact", {"mobile_no": mobile_no })
#     # if mobile_contact_name and user.email:
#     # 	mob_contact =  frappe.get_doc("Contact", mobile_contact_name)
#     # 	mob_contact.add_email(user.email, is_primary=True)
#     # 	mob_contact.save(ignore_permissions=True)

#     for d in frappe.get_list(
#         "Contact",
#         fields=("name"),
#         or_filters={"email_id": user.email, "user": user.email, "mobile_no": mobile_no},
#     ):
#         contact_name = frappe.db.get_value("Contact", d.name)
#         if contact_name:
#             contact = frappe.get_doc("Contact", contact_name)
#             doctypes = [d.link_doctype for d in contact.links]
#             tosave = False
#             if not contact.mobile_no:
#                 contact.mobile_no = mobile_no
#                 tosave = True
#             if not contact.email_id or not contact.user:
#                 contact.email_id = user
#                 contact.user = user
#                 contact.add_email(user, is_primary=True)
#                 tosave = True
#             if tosave:
#                 contact.save(ignore_permissions=True)
#                 frappe.db.commit()
#                 return

#     contact_name = get_contact_name(user.email)
#     if not contact_name:
#         contact = frappe.get_doc(
#             {
#                 "doctype": "Contact",
#                 "first_name": user.first_name,
#                 "last_name": user.last_name,
#                 "user": user.name,
#                 "gender": user.gender,
#             }
#         )

#         if user.email:
#             contact.add_email(user.email, is_primary=True)

#         if user.phone:
#             contact.add_phone(user.phone, is_primary_phone=True)

#         if user.mobile_no:
#             contact.add_phone(user.mobile_no, is_primary_mobile_no=True)
#         contact.insert(
#             ignore_permissions=True,
#             ignore_links=ignore_links,
#             ignore_mandatory=ignore_mandatory,
#         )
#     else:
#         contact = frappe.get_doc("Contact", contact_name)
#         contact.first_name = user.first_name
#         contact.last_name = user.last_name
#         contact.gender = user.gender

#         # Add mobile number if phone does not exists in contact
#         if user.phone and not any(
#             new_contact.phone == user.phone for new_contact in contact.phone_nos
#         ):
#             # Set primary phone if there is no primary phone number
#             contact.add_phone(
#                 user.phone,
#                 is_primary_phone=not any(
#                     new_contact.is_primary_phone == 1
#                     for new_contact in contact.phone_nos
#                 ),
#             )

#         # Add mobile number if mobile does not exists in contact
#         if user.mobile_no and not any(
#             new_contact.phone == user.mobile_no for new_contact in contact.phone_nos
#         ):
#             # Set primary mobile if there is no primary mobile number
#             contact.add_phone(
#                 user.mobile_no,
#                 is_primary_mobile_no=not any(
#                     new_contact.is_primary_mobile_no == 1
#                     for new_contact in contact.phone_nos
#                 ),
#             )

#         contact.save(ignore_permissions=True)