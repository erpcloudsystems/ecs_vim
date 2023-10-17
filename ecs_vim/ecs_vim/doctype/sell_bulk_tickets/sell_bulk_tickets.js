// Copyright (c) 2023, ERPCloud.systems and contributors
// For license information, please see license.txt

frappe.ui.form.on('Sell Bulk Tickets', {
	// refresh: function(frm) {

	// }
});


frappe.ui.form.on("Sell Bulk Tickets", "print_sales_invoice", function(frm){
	const sales_invoice = []
	frm.doc.sales_invoice.forEach(element => {
		sales_invoice.push(element.sales_invoice)
	});
	console.log(encodeURIComponent(sales_invoice.toString()))
	const link_print = `/api/method/frappe.utils.print_format.download_multi_pdf?doctype=Sales%20Invoice&name=${JSON.stringify(sales_invoice)}&format=Standard&no_letterhead=0&letterhead=VIM%20Letter%20Head&options=%7B%22page-size%22%3A%22A4%22%7D`
	window.open(link_print);
	window.print()
});

frappe.ui.form.on("Sell Bulk Tickets", "booklet", function(frm){
	// cur_frm.clear_table("items");   
	frappe.db.get_value("Booklets", frm.doc.booklet, ["item", "no_of_tickets"], function(response) {
		var d = frm.add_child("items");
		console.log(d)
		d.item_code = response.item;
		d.qty = response.no_of_tickets;
		cur_frm.refresh_field("items");
	})

});
frappe.ui.form.on("Ticket Sales Inovice", "cancel_invoice", function(frm,cdt,cdn) {
    {
		populate_je_obj(frm)
    }

        function populate_je_obj(frm, data) {
        var d = locals[cdt][cdn];
        let si = {};
		frappe.call(
			{
				method: "ecs_vim.ecs_vim.doctype.sell_bulk_tickets.sell_bulk_tickets.cancel_sales_invoice",
				args:{
					name:d.name,
					sales_invoice:d.sales_invoice,
				},
				callback: function (r){
					
				}
			}
		)

    
    }
    
    });