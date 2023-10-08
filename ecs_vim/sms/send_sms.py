import frappe, json
from frappe.core.doctype.sms_settings.sms_settings import send_sms
from frappe.utils import cstr


@frappe.whitelist()
def send_invoice_sms(mobile_no,name,type):
	recv_list=[mobile_no]
	send_sms(recv_list, cstr('Thank you for your purchase, your invoice is ready! ' + frappe.utils.get_url() + '/printview?doctype=POS%20Invoice&name={name}&trigger_print=1&format=new%20POS%20with%20QR&no_letterhead=0&letterhead=VIM%20Letter%20Head&settings=%7B%7D&_lang=en/'.format(name=name)  ))
