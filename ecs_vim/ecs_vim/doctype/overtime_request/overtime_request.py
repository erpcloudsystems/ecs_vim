# Copyright (c) 2023, ERPCloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class OvertimeRequest(Document):
	def on_submit(self):
		extra_salary = frappe.new_doc('Extra Salary')
		extra_salary.ref_doctype = "Overtime Request"
		extra_salary.employee = self.employee
		extra_salary.company = frappe.db.get_value("Employee", self.employee, "company")
		extra_salary.salary_component = "No of Overtime Hours"
		extra_salary.payroll_date = self.ot_request_date
		extra_salary.amount = self.ot_hours
		extra_salary.insert()
		extra_salary.submit()
