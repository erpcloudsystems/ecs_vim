# Copyright (c) 2023, ERPCloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Booklets(Document):
	def before_save(self):
		booklet_code = 1
		last_code = frappe.db.sql(
			"""
			SELECT code FROM `tabBooklets` ORDER BY code DESC LIMIT 1""",
			as_dict=1,
		)
		if last_code:
			booklet_code = last_code[0].code + 1

		self.code = booklet_code
		self.__set_name(self.code)
		self.__set_booklet_name(self.code)
		self.is_booklet = True

	def before_submit(self):
		self.__generate_tickets()
		self.item = self.__create_new_item(self.name)
		

	def __set_name(self, booklet_code):
		if self.name is None:
			new_name = "B" + str(booklet_code)
			self.name = new_name
		else:
			new_name = "B" + str(booklet_code)
			frappe.db.set_value("Booklets", self.name, "name", new_name)
			self.name = new_name


	def __set_booklet_name(self, booklet_code):
		if self.booklet_name is None:
			self.__set_name(booklet_code)
			self.booklet_name = self.name


	# create new item in item doctype and return its name
	def __create_new_item(self, item_name):
		item = frappe.new_doc("Item")
		item.item_name = item_name
		item.item_code = item_name
		item.item_group = "Booklet"
		
		item.custom_is_booklet = True
		# item.is_stock_item = True
		# item.include_item_in_manufacturing = True

		item.stock_uom = "Set"

		item.insert()
		item.submit()
		return item.name
	
	def __create_new_ticket(self, ticket_code):
		ticket = frappe.new_doc("Tickets")
		ticket.code = ticket_code
		ticket.ticket_name= f"{self.name}T{ticket_code}"
		ticket.barcode = ticket.ticket_name
		ticket.booklet = self.name
		ticket.item = self.item

		ticket.branches_ticket = self.branches_ticket
		ticket.insert()
		return ticket.name

	def __generate_tickets(self):
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
			code_tickets += 1
			ticket_name = self.__create_new_ticket(code_tickets)

			self.append("tickets",
				{
					"tickets": ticket_name
				}
			)
			no_of_tickets -=1
		
