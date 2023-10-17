# Copyright (c) 2023, ERPCloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CreateBulkTickets(Document):
	@frappe.whitelist()
	def before_submit(self):
		booklets_needed = self.no_of_tickets // self.no_of_tickets_per_booklet
		remaining_tickets = self.no_of_tickets %  self.no_of_tickets_per_booklet
		code_booklets = 0
		last_code = frappe.db.sql(
			"""
			SELECT code FROM `tabBooklets` ORDER BY creation DESC LIMIT 1""",
			as_dict=1,
		)
		if last_code :
			code_booklets = last_code[0].code
		while booklets_needed > 0:
			booklets = frappe.new_doc("Booklets")
			booklets.no_of_tickets = self.no_of_tickets_per_booklet
			code_booklets += 1
			booklets.code = code_booklets
			booklets.booklet_name= f"B{booklets.code}"
			booklets.branches_ticket = self.branches_ticket
			booklets.item = self.item
			booklets.insert()
			booklets.submit()
			booklets_needed -=1
		
		if remaining_tickets:
			booklets = frappe.new_doc("Booklets")
			booklets.no_of_tickets = remaining_tickets
			code_booklets += 1
			booklets.code = code_booklets
			booklets.booklet_name= f"B{booklets.code}"
			booklets.branches_ticket = self.branches_ticket
			booklets.insert()
			booklets.submit()
	pass
