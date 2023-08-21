var send_invoice_sms=0;
var sales_invoice=0;
frappe.ui.form.on('Sales Invoice', {
    refresh:function(frm){
      
       frappe.db.get_single_value('Selling Settings', 'send_invoice_sms').then(function(val) {
        send_invoice_sms=val;
    });
      
    frappe.db.get_single_value('Selling Settings', 'sales_invoice').then(function(val) {
        sales_invoice=val;
    });
  
    },
    on_submit:function(frm){
        if(frm.doc.docstatus==1)
        {
            frm.trigger("make_dialog")
        }
        
    },
    make_dialog:function(frm){
     
        console.log(send_invoice_sms,sales_invoice)
        if(send_invoice_sms==1 && sales_invoice==1){
            frappe.call({
                method: "frappe.client.get_value",
                args: {
                "doctype": "Customer",
                "filters": {"name":frm.doc.customer},
                "fieldname": "mobile_no"
                }, callback: function(r) {
                
                const dialog = new frappe.ui.Dialog({
                    title: __('Send sms to'),
                    static: true,
                    fields: [
                        {
                            fieldtype: 'Link', label: __('Customer'), fieldname: 'customer_name',
                            options: 'Customer', reqd: 1,default:frm.doc.customer,read_only:1
                        },
                        {
                            fieldtype: 'Int', label: __('Mobile No'),
                             fieldname: 'mobile_no', reqd: 1,default:r.message["mobile_no"]
                        },
                      
                    ],
                    primary_action: async function({ customer_name,mobile_no }) {
                            
                                if(mobile_no.toString().length < 10 || mobile_no.toString().length > 10){
                                    frappe.throw("Invalid Mobile No !!")
                                }
                                return frappe.call({
                                    method: "invoice_sms.sms.send_sms.send_invoice_sms",
                                    args: {
                                        'mobile_no': mobile_no,
                                        'name': frm.doc.name,
                                        'type':'INV'
                                    },
                                    callback(res) {
                                        
                                        dialog.hide();
                                    }
                                });
                      
                    },
                    primary_action_label: __('Submit')
                });
              
                }});
        }
       
    }
})

