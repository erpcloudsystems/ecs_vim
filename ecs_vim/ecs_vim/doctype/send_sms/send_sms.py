# Copyright (c) 2023, ERPCloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe import _, msgprint
from frappe.core.doctype.sms_settings.sms_settings import send_sms
from frappe.model.document import Document
from frappe.utils import cstr

class SendSMS(Document):

	@frappe.whitelist()
	def create_receiver_list(self):
		frappe.msgprint(_("Creating Receiver List"))
		rec, where_clause = "", ""
		if self.send_to == "All Customer Contact":
			where_clause = " and dl.link_doctype = 'Customer'"
			if self.customer:
				where_clause += (
					" and dl.link_name = '%s'" % self.customer.replace("'", "'")
					or " and ifnull(dl.link_name, '') != ''"
				)
		if self.send_to == "All Supplier Contact":
			where_clause = " and dl.link_doctype = 'Supplier'"
			if self.supplier:
				where_clause += (
					" and dl.link_name = '%s'" % self.supplier.replace("'", "'")
					or " and ifnull(dl.link_name, '') != ''"
				)
		if self.send_to == "All Sales Partner Contact":
			where_clause = " and dl.link_doctype = 'Sales Partner'"
			if self.sales_partner:
				where_clause += (
					"and dl.link_name = '%s'" % self.sales_partner.replace("'", "'")
					or " and ifnull(dl.link_name, '') != ''"
				)
		if self.send_to in [
			"All Contact",
			"All Customer Contact",
			"All Supplier Contact",
			"All Sales Partner Contact",
		]:
			rec = frappe.db.sql(
				f"""select CONCAT(ifnull(c.first_name,''), ' ', ifnull(dl.link_title,'')),
				c.mobile_no from `tabContact` c, `tabDynamic Link` dl  where ifnull(c.mobile_no,'')!='' and
				c.docstatus != 2 and dl.parent = c.name {where_clause}
				and c.creation between '{self.from_date}' and '{self.to_date}'"""
			)

		elif self.send_to == "All Lead (Open)":
			rec = frappe.db.sql(
				"""select lead_name, mobile_no from `tabLead` where
				ifnull(mobile_no,'')!='' and docstatus != 2 and status='Open'"""
			)

		elif self.send_to == "All Employee (Active)":
			where_clause = (
				self.department and " and department = '%s'" % self.department.replace("'", "'") or ""
			)
			where_clause += self.branch and " and branch = '%s'" % self.branch.replace("'", "'") or ""

			rec = frappe.db.sql(
				"""select employee_name, cell_number from
				`tabEmployee` where status = 'Active' and docstatus < 2 and
				ifnull(cell_number,'')!='' %s"""
				% where_clause
			)

		elif self.send_to == "All Sales Person":
			rec = frappe.db.sql(
				"""select sales_person_name,
				tabEmployee.cell_number from `tabSales Person` left join tabEmployee
				on `tabSales Person`.employee = tabEmployee.name
				where ifnull(tabEmployee.cell_number,'')!=''"""
			)

		rec_list = ""
		for d in rec:
			rec_list += d[0] + " - " + d[1] + "\n"
		self.receiver_list = rec_list
	def get_receiver_nos(self):
		receiver_nos = []
		if self.receiver_list:
			for d in self.receiver_list.split("\n"):
				receiver_no = d
				if "-" in d:
					receiver_no = receiver_no.split("-")[1]
				if receiver_no.strip():
					receiver_nos.append(cstr(receiver_no).strip())
		else:
			msgprint(_("Receiver List is empty. Please create Receiver List"))

		return receiver_nos
	
	def is_customer(self, receiver_list):
		customers = []
		non_customers = []
		for receiver in receiver_list:
			customer = frappe.db.get_value("Customer", {"mobile_no": receiver})
			if customer:
				customers.append(customer)
			else:
				non_customers.append(receiver)
		return customers, non_customers
	
	@frappe.whitelist()
	def send_sms(self):
		receiver_list = []
		
		receiver_list = self.get_receiver_nos()
		main_message = self.message
		if receiver_list:
			customers, non_customers = self.is_customer(receiver_list)
			if customers:
				message = "Link: https://erp.vim.sa/customer-details/new?mobile_no=23032032032&customer=ss"
				if main_message:
					message += "\n" + main_message
				send_sms(receiver_list, cstr(message))
			if non_customers:
				message = "Link: https://erp.vim.sa/customer-details/new?"
				if main_message:
					message += "\n" + main_message
				send_sms(receiver_list, cstr(message))