// Copyright (c) 2023, ERPCloud.systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["total Monthly Sales Summary Statement"] = {
	"filters": [
        {
            "fieldname": "from_date",
            "label": __("From Date"),
            "fieldtype": "Date",
			"default": frappe.datetime.add_months(frappe.datetime.get_today(), -1)
        },
        {
            "fieldname": "to_date",
            "label": __("To Date"),
            "fieldtype": "Date",
			"default": frappe.datetime.get_today()
        },
	]
};
