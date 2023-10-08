// Copyright (c) 2023, ERPCloud.systems and contributors
// For license information, please see license.txt

frappe.ui.form.on('Send SMS', {
	onload: function (frm) {
		// set from date and to date 
		frm.set_value("from_date", frappe.datetime.add_months(frappe.datetime.get_today(), -1));
		frm.set_value("to_date", frappe.datetime.get_today());
	},
	message: function (frm) {
		var total_characters = frm.doc.message.length;
		var total_msg = 1;

		if (total_characters > 160) {
			total_msg = cint(total_characters / 160);
			total_msg = (total_characters % 160 == 0 ? total_msg : total_msg + 1);
		}

		frm.set_value("total_characters", total_characters);
		frm.set_value("total_messages", frm.doc.message ? total_msg : 0);
	}
});

