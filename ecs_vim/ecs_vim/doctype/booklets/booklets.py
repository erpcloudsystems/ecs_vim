# Copyright (c) 2023, ERPCloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Booklets(Document):
	def before_submit(self):
		no_of_tickets = self.no_of_tickets 
		code_tickets = 0
		last_code = frappe.db.sql(
			"""
			SELECT code FROM `tabTickets` ORDER BY creation DESC LIMIT 1""",
			as_dict=1,
		)
		if last_code :
			code_tickets = last_code[0].code
		while no_of_tickets > 0:
			tickets = frappe.new_doc("Tickets")
			code_tickets += 1
			tickets.code = code_tickets
			tickets.ticket_name= f"{self.name}T{tickets.code}"
			tickets.barcode= tickets.ticket_name
			tickets.booklet = self.name
			tickets.item = self.item

			tickets.branches_ticket = self.branches_ticket
			tickets.insert()
			self.append("tickets",
				{
					"tickets": tickets.name
				}
			)
			no_of_tickets -=1
			# tickets = frappe.new_doc("Tickets")
		pass
	pass
