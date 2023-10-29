import frappe
import requests
import json 
from frappe.utils.password import check_password, get_password_reset_limit
from frappe.rate_limiter import rate_limit


class OTP():
    def __init__(self, phonenumber):
        self.api_params = OTP.get_api_params()
        self.base_url = "http://REST.GATEWAY.SA/api/"
        self.api_id =  self.api_params.get("api_id")
        self.api_password =  self.api_params.get("api_password")
        self.brand = self.api_params.get("sms_text")
        self.country_code = self.api_params.get("country_code")
        self.sender_id = self.api_params.get("sender_id")
        self.phonenumber = self.clean(phonenumber)
    def clean(self, phonenumber):
        if phonenumber.startswith(self.country_code):
            return phonenumber.removeprefix(self.country_code)
        return phonenumber
    @staticmethod
    def get_api_params():
        parameters = frappe.get_doc("SMS Settings")
        api_params = {}
        for row in parameters.parameters:
            api_params[row.parameter] = row.value
        return api_params
    
    def send_otp(self):
        params = {
            "api_id": self.api_id,
            "api_password":self.api_password,
            "brand":self.brand,
            "phonenumber":self.country_code  + self.phonenumber,
            "sender_id": self.sender_id,
        }
        response = requests.get(self.base_url + "Verify", params=params)
        if response:
            return response.json()
        else:
            return {"error": "no response found"}

    @staticmethod
    def update_session_otp_status(user_ip, response):
        if response["verfication_id"]:
            user_ip.sent = 1
            user_ip.status = response["status"]
            user_ip.remarks = response["remarks"]
            user_ip.verfication_id = response["verfication_id"]
            user_ip.save(ignore_permissions=True)
            frappe.db.commit()
    
    @staticmethod
    def checking_verification_status(otp_doc, otp):
        params = {
            "verfication_id": str(otp_doc.verfication_id),
            "verfication_code": str(otp),
        }
        response = requests.get("http://REST.GATEWAY.SA/api/" + "VerifyStatus", params=params)
        if response:
            return response.json()

        else:
            return {"error": "no response found"}
def get_context(context):
    # get current user session data
    user_ip = frappe.get_doc("Session OTP Users", frappe.form_dict.docname)
    context.user_ip = user_ip
    
    if user_ip.phone_no and not user_ip.sent:
        otp = OTP(user_ip.phone_no)
        response = otp.send_otp()
        context.response = str(response)
        context.country_code = otp.country_code
        context.phonenumber = otp.phonenumber
        OTP.update_session_otp_status(user_ip, response)
    else:
        context.response = "Message Already sent Please Wait"


    return context

@frappe.whitelist(allow_guest=True)
@rate_limit(limit=20000, seconds=24 * 60 * 60)
def verify_otp(otp, session_doc):

    user_ip = frappe.local.request_ip
    if frappe.db.exists("Session OTP Users", {"name":session_doc}):
        session_otp_user = frappe.get_doc("Session OTP Users", session_doc)
        if session_otp_user.sent:
            response = OTP.checking_verification_status(session_otp_user, otp)
            if response:
                user = frappe.get_doc("User", session_otp_user.user)
                ## update contact verified
                contact = frappe.get_doc("Contact", {"user":user.name})
                contact_phone = frappe.get_doc("Contact Phone", {"parent":contact.name, "is_primary_mobile_no":1,"phone":session_otp_user.phone_no } )
                contact_phone.custom_is_verified = 1
                contact_phone.save(ignore_permissions=True)
                return  response , user.reset_password()
            else:
                return "Message Already sent Please Wait"
