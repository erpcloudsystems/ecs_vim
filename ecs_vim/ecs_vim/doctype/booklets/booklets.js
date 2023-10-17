// Copyright (c) 2023, ERPCloud.systems and contributors
// For license information, please see license.txt

frappe.ui.form.on('Booklets', {
	// refresh: function(frm) {

	// }
});
frappe.ui.form.on("Booklets", "print_tickets", function(frm){
	const tickets = []
	frm.doc.tickets.forEach(element => {
		tickets.push(element.tickets)
	});
	const link_print = `/api/method/frappe.utils.print_format.download_multi_pdf?doctype=Tickets&name=${JSON.stringify(tickets)}&format=Standard&no_letterhead=0&letterhead=VIM%20Letter%20Head&options=%7B%22page-size%22%3A%22A4%22%7D`
	window.open(link_print);
});
