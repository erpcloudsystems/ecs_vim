// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Manger Follow Up Report For Leads"] = {
	"filters": [
	
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"width": "80"
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"width": "80"
		},

		{
			"fieldname":"lead",
			"label": __("Lead"),
			"fieldtype": "Link",
			"options" : "Lead",
			"reqd": 0
		},
		{
			"fieldname":"sales_person",
			"label": __("Sales Person"),
			"fieldtype": "Link",
			"options" : "Sales Person",
			"reqd": 0
		},
		// {
		// 	"fieldname":"last_lead_follow_up_sales_person",
		// 	"label": __("Last Lead Follow Up Sales Person"),
		// 	"fieldtype": "Link",
		// 	"options" : "Sales Person",
		// 	"reqd": 0
		// }
	]
}