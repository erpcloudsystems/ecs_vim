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
    user_session = frappe.session.user
    # if user_session != "Guest":
    #     customer = frappe.get_doc("Customer", {"mobile_no": user.mobile_no})
    #     if customer.custom_finished_details == 1:
    #         context.redirect = True 
    #     context.redirect = False




def prepare_input_values(context, user):
    customer = frappe.get_doc("Customer", {"mobile_no": user.mobile_no})
    customer.custom_user == user.name
    # if not customer.last_name:
    #     customer.last_name = user.name.split("@")[0]
    customer.save(ignore_permissions=True)
    # no he have customer and user docs
    # initialize DOM inputs
    context.first_name = user.first_name or ""
    context.last_name  = customer.last_name or ""
    context.email  = user.email or ""
    context.mobile_no  = user.mobile_no or ""
    context.relation  = customer.customer_family_detail[0].relation or "" if len(customer.customer_family_detail)>0 else ""
    context.address  = frappe.db.get_value("Address", customer.customer_primary_address, ["address_line1"]) or ""
    context.gender  = customer.customer_family_detail[0].gender or "" if len(customer.customer_family_detail)>0 else ""
    context.nationality  = customer.nationality or ""
    context.custom_branch  = customer.custom_branch or ""
    context.dob  = customer.customer_family_detail[0].dob or "" if len(customer.customer_family_detail)>0 else ""
    context.custom_finished_details  = customer.custom_finished_details
    context.first_name2 = ""
    context.last_name2  = ""
    context.email2  = ""
    context.mobile_no2  = ""
    context.relation2  = ""
    context.address2  = ""
    context.gender2  =  ""
    context.nationality2  = ""
    context.custom_branch2  = ""
    context.dob2  = ""
    if len(customer.customer_family_detail)>1 and customer.customer_family_detail[1].adult:
        context.first_name2 = customer.customer_family_detail[1].first_name or ""
        context.last_name2  = customer.customer_family_detail[1].last_name or ""
        context.email2  = customer.customer_family_detail[1].email_id or ""
        context.mobile_no2  = customer.customer_family_detail[1].phone_no or ""
        context.relation2  = customer.customer_family_detail[1].relation or "" 
        context.address2  = frappe.db.get_value("Address", customer.customer_family_detail[1].address, ["address_line1"]) or ""
        context.gender2  =  customer.customer_family_detail[1].gender or "" 
        context.nationality2  = customer.customer_family_detail[1].nationality or ""
        context.custom_branch2  = customer.customer_family_detail[1].branch or ""
        context.dob2  = customer.customer_family_detail[1].dob or "" 
    context.first_name3 = ""
    context.fav_char = ""
    context.dob3 = ""
    context.gender3 = ""
    context.school_name3 = ""
    context.fav_color3 = ""
    context.other_color = ""
    for row in customer.customer_family_detail:
        if row.child:
            context.first_name3 = row.child_name
            context.fav_char = row.favorite_character
            context.dob3 = row.dob
            context.gender3 = row.gender
            context.school_name3 = row.school_name
            context.fav_color3 = row.favourite_colour
            context.other_color = row.other_colour


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
        user = frappe.get_doc("User", frappe.session.user)  

        customer = frappe.get_doc("Customer", {"mobile_no": user.mobile_no})
        customer.custom_finished_details = 1
        customer.flags.ignore_mandatory = True
        customer.db_update()

@frappe.whitelist(allow_guest=True)
def checked_finished_details():
    user = frappe.session.user
    user = frappe.get_doc("User", frappe.session.user)  

    if user.name != "Guest":
        customer = frappe.get_doc("Customer", {"mobile_no": user.mobile_no})
        if customer.custom_finished_details == 1:
            return "/customer-details"
    return False

from abc import ABC, abstractmethod


class Customer:
    def __init__(self, user):
        self.user = user

    @staticmethod
    def get_customer_doc(customer_id):
        return frappe.get_doc("Customer", customer_id)
    def get_customer_assigned_to_user(self):
        try:
            self.customer_id = frappe.db.get_value("Customer", {"email_id": self.user }, ["name"])
        except:
            self.customer_id = None
    def create_address(self):
        doc = frappe.get_doc({
                "doctype":"Address",
                "address_type":"Billing",
                "address_line1": self.kwargs.get("customer_primary_address"),
                "country":self.kwargs.get("territory"),
                "city":self.kwargs.get("territory"),
                "links": [ {
                    "link_doctype":"Customer",
                    "link_name":self.customer.name,
                }],
            })
        doc.insert(ignore_permissions=True)
        return doc.name

    def assign_values(self, **kwargs):
        if kwargs:
            self.kwargs = kwargs
            self.customer = Customer.get_customer_doc(self.customer_id) if self.customer_id else None
            self.customer.first_name = kwargs.get("first_name")
            self.customer.last_name = kwargs.get("last_name")
            self.customer.custom_branch = kwargs.get("custom_branch")
            self.customer.nationality = kwargs.get("territory")
            address_name = self.create_address()
            self.customer.customer_primary_address = address_name
            if len(self.customer.customer_family_detail) > 0:
                self.customer.customer_family_detail[int(kwargs.get("page"))].first_name = kwargs.get("first_name")
                self.customer.customer_family_detail[int(kwargs.get("page"))].last_name = kwargs.get("last_name")
                self.customer.customer_family_detail[int(kwargs.get("page"))].dob = kwargs.get("dob")
                self.customer.customer_family_detail[int(kwargs.get("page"))].email_id = kwargs.get("email_id")
                self.customer.customer_family_detail[int(kwargs.get("page"))].gender = kwargs.get("gender")
                self.customer.customer_family_detail[int(kwargs.get("page"))].phone_no = kwargs.get("mobile_no")
                self.customer.customer_family_detail[int(kwargs.get("page"))].relation = kwargs.get("relation")
                self.customer.customer_family_detail[int(kwargs.get("page"))].branch = kwargs.get("custom_branch")
                self.customer.customer_family_detail[int(kwargs.get("page"))].address = address_name
                self.customer.customer_family_detail[int(kwargs.get("page"))].nationality = kwargs.get("territory")
            # self.customer.save(ignore_permissions=True)
            self.customer.db_update()


        return self.customer
    def add_another_person(self, **kwargs):
        if kwargs:
            self.kwargs = kwargs
            self.customer = Customer.get_customer_doc(self.customer_id) if self.customer_id else None
            address_name = self.create_address()
            if len(self.customer.customer_family_detail) > 1:
                self.customer.customer_family_detail[int(kwargs.get("page"))].first_name = kwargs.get("first_name")
                self.customer.customer_family_detail[int(kwargs.get("page"))].last_name = kwargs.get("last_name")
                self.customer.customer_family_detail[int(kwargs.get("page"))].person_name =  kwargs.get("first_name") + " " + kwargs.get("last_name")
                self.customer.customer_family_detail[int(kwargs.get("page"))].dob = kwargs.get("dob")
                self.customer.customer_family_detail[int(kwargs.get("page"))].email_id = kwargs.get("email_id")
                self.customer.customer_family_detail[int(kwargs.get("page"))].gender = kwargs.get("gender")
                self.customer.customer_family_detail[int(kwargs.get("page"))].phone_no = kwargs.get("mobile_no")
                self.customer.customer_family_detail[int(kwargs.get("page"))].relation = kwargs.get("relation")
                self.customer.customer_family_detail[int(kwargs.get("page"))].branch = kwargs.get("custom_branch")
                self.customer.customer_family_detail[int(kwargs.get("page"))].address = address_name
                self.customer.customer_family_detail[int(kwargs.get("page"))].nationality = kwargs.get("territory")
            else:
                self.customer.append("customer_family_detail", {
                    "adult":1,
                    "first_name": kwargs.get("first_name"),
                    "last_name": kwargs.get("last_name"),
                    "person_name": kwargs.get("first_name") + " " + kwargs.get("last_name"),
                    "relation": kwargs.get("relation"),
                    "gender": kwargs.get("gender"),
                    "dob": kwargs.get("dob"),
                    "phone_no": kwargs.get("mobile_no"),
                    "email_id": kwargs.get("email_id"),
                    "branch": kwargs.get("custom_branch"),
                    "address": address_name,
                    "nationality": kwargs.get("territory"),
                })
            # self.customer.save(ignore_permissions=True)
            self.customer.db_update()

        return self.customer
    def add_child(self, **kwargs):
        if kwargs:
            self.kwargs = kwargs
            self.customer = Customer.get_customer_doc(self.customer_id) if self.customer_id else None
            update = True
            for row in self.customer.customer_family_detail:
                if row.child:
                    update = False
                    row.gender = kwargs.get("gender")
                    row.dob = kwargs.get("dob")
                    row.school_name = kwargs.get("first_name")
                    row.child_name = kwargs.get("customer_primary_address")
                    row.favorite_character = ",".join(['Cars', 'PJ Mask', 'Toy Story']) if kwargs.get("territory") else None,
                    row.favourite_colour = kwargs.get("relation")
                    row.other_colour = kwargs.get("mobile_no")

            if update:
                self.customer.append("customer_family_detail", {
                    "child":1,
                    "gender": kwargs.get("gender"),
                    "dob": kwargs.get("dob"),
                    "school_name": kwargs.get("first_name"),
                    "child_name": kwargs.get("customer_primary_address"),
                    "favorite_character": ",".join(['Cars', 'PJ Mask', 'Toy Story']) if kwargs.get("territory") else None,
                    "favourite_colour": kwargs.get("relation"),
                    "other_colour": kwargs.get("mobile_no"),
                })
            # self.customer.save(ignore_permissions=True)
            self.customer.db_update()


        return self.customer

# this function called every click on استمرار button in fron end also comming with payload of form data
@frappe.whitelist()
def update_customer(inputparams): # "{"key":"value"}"
    import ast
    data = ast.literal_eval(inputparams)
    customer = Customer(frappe.session.user)
    customer.get_customer_assigned_to_user()
    if customer and data["page"] == "0":
        args = customer.assign_values(**data)
        return args
    if customer and data["page"] == "1":
        args = customer.add_another_person(**data)
        return args
    if customer and data["page"] == "2":
        args = customer.add_child(**data)
        return args
    frappe.db.commit()
