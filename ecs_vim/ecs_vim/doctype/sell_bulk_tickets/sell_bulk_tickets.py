# Copyright (c) 2023, ERPCloud.systems and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from unittest.util import sorted_list_difference
import frappe
import json
from frappe.model.document import Document
from erpnext.setup.utils import get_exchange_rate
from datetime import date
import datetime

class SellBulkTickets(Document):

	@frappe.whitelist()
	def before_submit(self):
		y = frappe.get_doc("Sell Bulk Tickets", self.name)
		frappe.msgprint(f"{self.name}")
		frappe.msgprint(f"{y.items[0].item_code}")

		qty = self.quantity
		self.sales_invoice=[]
		while qty > 0:
			invoice = self.create_invoice()
			
			self.append("sales_invoice",
				{
					"sales_invoice": invoice.name
				}
			)
			# frappe.db.sql(

			# 	f"""
			# 		INSERT INTO `tabTicket Sales Inovice` (parentfield, parenttype, parent, sales_invoice,status )
			# 			VALUES ('sales_invoice', 'Sell Bulk Tickets', '{self.name}', '{invoice.name}', '{invoice.status}' );	
			# 	"""
			# )
			qty -= 1
		pass
	def create_invoice(self):
		sales_invoice = frappe.new_doc("Sales Invoice")
		sales_invoice.customer = self.customer
		for x in self.items:
			items = sales_invoice.append("items", {})
			items.item_code = x.item_code
			items.rate = x.rate
			items.qty = x.qty
			items.description = x.description

		sales_invoice.insert()
		sales_invoice.submit()
		return sales_invoice
	
@frappe.whitelist()
def cancel_sales_invoice(name, sales_invoice):
	sales_invoice = frappe.get_doc("Sales Invoice", sales_invoice)
	sales_invoice.cancel()
	frappe.db.sql(f"""
		UPDATE `tabTicket Sales Inovice` set is_cancelled = 1 where name = '{name}'
	""")
	pass