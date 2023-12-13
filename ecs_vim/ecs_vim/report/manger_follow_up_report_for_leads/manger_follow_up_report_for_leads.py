# Copyright (c) 2013, erpcloud.systems and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _


def execute(filters=None):
	columns, data = [], []
	columns = get_columns()
	data = get_data(filters, columns)
	return columns, data


def get_columns():
	return [
		{
			"label": _("Lead"),
			"fieldname": "lead",
			"fieldtype": "Link",
			"options": "Lead",
			"width": 180
		},
		{
			"label": _("Follow Up Date"),
			"fieldname": "date",
			"fieldtype": "Date",
			"width": 180
		},
		{
			"label": _("Follow-up Report"),
			"fieldname": "call_details",
			"fieldtype": "Data",
			"width": 180
		},
		{
			"label": _("Next Follow Up Date"),
			"fieldname": "next_follow_up_date",
			"fieldtype": "Date",
			"width": 180
		},
		{
			"label": _("Status"),
			"fieldname": "status",
			"fieldtype": "Data",
			"width": 180
		},
		{
			"label": _("sales_person"),
			"fieldname": "sales_person",
			"fieldtype": "Link",
			"options": "Sales Person",
			"width": 180
		},

		



	]


def get_data(filters, columns):
	item_price_qty_data = []
	item_price_qty_data = get_item_price_qty_data(filters)
	return item_price_qty_data


def get_item_price_qty_data(filters):
	conditions = ""
	conditions2 = ""
	if filters.get("from_date"):
		conditions += " and `tabLead Follow Up`.next_follow_up_date >=%(from_date)s"
	if filters.get("to_date"):
		conditions += " and `tabLead Follow Up`.next_follow_up_date <=%(to_date)s"
	if filters.get("sales_person"):
		conditions += " and `tabLead Follow Up`.sales_person =%(sales_person)s"
	if filters.get("last_lead_follow_up_sales_person"):
		conditions += " and `tabLead Follow Up`.last_lead_follow_up_sales_person =%(last_lead_follow_up_sales_person)s"
	if filters.get("lead"):
		conditions += " and `tabLead Follow Up`.lead =%(lead)s"
	result = []

	item_results = frappe.db.sql("""
			select 
					`tabLead Follow Up`.lead as lead,
					IFNULL(`tabLead Follow Up`.date, "00-00-0000") as date,
					IFNULL(`tabLead Follow Up`.call_details,"No Details") as call_details,
					IFNULL(`tabLead Follow Up`.sales_person,"No Sales Person" ) as sales_person,
					IFNULL(`tabLead Follow Up`.next_follow_up_date, "00-00-0000") as next_follow_up_date,
					IFNULL(`tabLead Follow Up`.status, "No Data") as status
					
					
			from
			       `tabLead Follow Up`  
			where
			  
			   `tabLead Follow Up`.docstatus = 1
			 {conditions}
			 {conditions2}
			 
			""".format(conditions=conditions,conditions2=conditions2), filters, as_dict=1)

# price_list_names = list(set([item.price_list_name for item in item_results]))

# buying_price_map = get_price_map(price_list_names, buying=1)
# selling_price_map = get_price_map(price_list_names, selling=1)


	if item_results:
		for item_dict in item_results:
			data = {
				'lead': item_dict.lead,
				'date': _(item_dict.date),
				'call_details': item_dict.call_details,
				'sales_person': _(item_dict.sales_person),
				'last_lead_follow_up_sales_person': _(item_dict.last_lead_follow_up_sales_person),
				'next_follow_up_date': _(item_dict.next_follow_up_date),
				'status': _(item_dict.status)

			}
			result.append(data)

	return result