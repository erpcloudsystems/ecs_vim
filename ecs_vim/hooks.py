from . import __version__ as app_version

app_name = "ecs_vim"
app_title = "Ecs Vim"
app_publisher = "ERPCloud.systems"
app_description = "customizations"
app_email = "info@erpcloud.systems"
app_license = "MIT"
fixtures = ["Custom Field", "Property Setter", "Print Format"]
# include assets
app_include_css = [
    "//cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css",
    "/assets/ecs_vim/css/ecs_vim.css",
]

# session creation
app_include_js = [
    "/assets/ecs_vim/js/customer_quick_entry.js",
    "//cdnjs.cloudflare.com/ajax/libs/echarts/4.8.0/echarts.min.js",
    "/assets/ecs_vim/js/frappe/ui/toolbar/search_utils.js",
    "//cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js",
]


on_session_creation = "ecs_vim.api.successful_login"

jenv = {
    "methods": [
        "get_qr:ecs_vim.doctype_triggers.qr_generate.get_qr",
        "get_out_time:ecs_vim.doctype_triggers.qr_generate.get_out_time",
    ]
}
calendars = ["Event Booking"]

# include js, css files in header of web template
web_include_css = [
    "/assets/ecs_vim/css/ecs_vim.css",
    "/assets/ecs_vim/css/ecs_vim-website.css",
]
doc_events = {
    "Journal Entry": {
        "before_insert": "ecs_vim.doctype_triggers.accounting.journal_entry.journal_entry.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.accounting.journal_entry.journal_entry.after_insert",
        "onload": "ecs_vim.doctype_triggers.accounting.journal_entry.journal_entry.onload",
        "before_validate": "ecs_vim.doctype_triggers.accounting.journal_entry.journal_entry.before_validate",
        "validate": "ecs_vim.doctype_triggers.accounting.journal_entry.journal_entry.validate",
        "on_submit": "ecs_vim.doctype_triggers.accounting.journal_entry.journal_entry.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.accounting.journal_entry.journal_entry.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.accounting.journal_entry.journal_entry.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.accounting.journal_entry.journal_entry.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.accounting.journal_entry.journal_entry.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.accounting.journal_entry.journal_entry.on_update",
    },
    "Payment Entry": {
        "before_insert": "ecs_vim.doctype_triggers.accounting.payment_entry.payment_entry.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.accounting.payment_entry.payment_entry.after_insert",
        "onload": "ecs_vim.doctype_triggers.accounting.payment_entry.payment_entry.onload",
        "before_validate": "ecs_vim.doctype_triggers.accounting.payment_entry.payment_entry.before_validate",
        "validate": "ecs_vim.doctype_triggers.accounting.payment_entry.payment_entry.validate",
        "on_submit": "ecs_vim.doctype_triggers.accounting.payment_entry.payment_entry.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.accounting.payment_entry.payment_entry.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.accounting.payment_entry.payment_entry.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.accounting.payment_entry.payment_entry.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.accounting.payment_entry.payment_entry.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.accounting.payment_entry.payment_entry.on_update",
    },
    "Purchase Invoice": {
        "before_insert": "ecs_vim.doctype_triggers.accounting.purchase_invoice.purchase_invoice.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.accounting.purchase_invoice.purchase_invoice.after_insert",
        "onload": "ecs_vim.doctype_triggers.accounting.purchase_invoice.purchase_invoice.onload",
        "before_validate": "ecs_vim.doctype_triggers.accounting.purchase_invoice.purchase_invoice.before_validate",
        "validate": "ecs_vim.doctype_triggers.accounting.purchase_invoice.purchase_invoice.validate",
        "on_submit": "ecs_vim.doctype_triggers.accounting.purchase_invoice.purchase_invoice.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.accounting.purchase_invoice.purchase_invoice.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.accounting.purchase_invoice.purchase_invoice.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.accounting.purchase_invoice.purchase_invoice.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.accounting.purchase_invoice.purchase_invoice.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.accounting.purchase_invoice.purchase_invoice.on_update",
    },
    "Sales Invoice": {
        "before_insert": "ecs_vim.doctype_triggers.accounting.sales_invoice.sales_invoice.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.accounting.sales_invoice.sales_invoice.after_insert",
        "onload": "ecs_vim.doctype_triggers.accounting.sales_invoice.sales_invoice.onload",
        "before_validate": "ecs_vim.doctype_triggers.accounting.sales_invoice.sales_invoice.before_validate",
        "validate": "ecs_vim.doctype_triggers.accounting.sales_invoice.sales_invoice.validate",
        "on_submit": "ecs_vim.doctype_triggers.accounting.sales_invoice.sales_invoice.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.accounting.sales_invoice.sales_invoice.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.accounting.sales_invoice.sales_invoice.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.accounting.sales_invoice.sales_invoice.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.accounting.sales_invoice.sales_invoice.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.accounting.sales_invoice.sales_invoice.on_update",
    },
    "Material Request": {
        "before_insert": "ecs_vim.doctype_triggers.buying.material_request.material_request.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.buying.material_request.material_request.after_insert",
        "onload": "ecs_vim.doctype_triggers.buying.material_request.material_request.onload",
        "before_validate": "ecs_vim.doctype_triggers.buying.material_request.material_request.before_validate",
        "validate": "ecs_vim.doctype_triggers.buying.material_request.material_request.validate",
        "on_submit": "ecs_vim.doctype_triggers.buying.material_request.material_request.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.buying.material_request.material_request.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.buying.material_request.material_request.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.buying.material_request.material_request.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.buying.material_request.material_request.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.buying.material_request.material_request.on_update",
    },
    "Purchase Order": {
        "before_insert": "ecs_vim.doctype_triggers.buying.purchase_order.purchase_order.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.buying.purchase_order.purchase_order.after_insert",
        "onload": "ecs_vim.doctype_triggers.buying.purchase_order.purchase_order.onload",
        "before_validate": "ecs_vim.doctype_triggers.buying.purchase_order.purchase_order.before_validate",
        "validate": "ecs_vim.doctype_triggers.buying.purchase_order.purchase_order.validate",
        "on_submit": "ecs_vim.doctype_triggers.buying.purchase_order.purchase_order.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.buying.purchase_order.purchase_order.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.buying.purchase_order.purchase_order.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.buying.purchase_order.purchase_order.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.buying.purchase_order.purchase_order.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.buying.purchase_order.purchase_order.on_update",
    },
    "Request For Quotation": {
        "before_insert": "ecs_vim.doctype_triggers.buying.request_for_quotation.request_for_quotation.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.buying.request_for_quotation.request_for_quotation.after_insert",
        "onload": "ecs_vim.doctype_triggers.buying.request_for_quotation.request_for_quotation.onload",
        "before_validate": "ecs_vim.doctype_triggers.buying.request_for_quotation.request_for_quotation.before_validate",
        "validate": "ecs_vim.doctype_triggers.buying.request_for_quotation.request_for_quotation.validate",
        "on_submit": "ecs_vim.doctype_triggers.buying.request_for_quotation.request_for_quotation.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.buying.request_for_quotation.request_for_quotation.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.buying.request_for_quotation.request_for_quotation.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.buying.request_for_quotation.request_for_quotation.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.buying.request_for_quotation.request_for_quotation.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.buying.request_for_quotation.request_for_quotation.on_update",
    },
    "Supplier": {
        "before_insert": "ecs_vim.doctype_triggers.buying.supplier.supplier.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.buying.supplier.supplier.after_insert",
        "onload": "ecs_vim.doctype_triggers.buying.supplier.supplier.onload",
        "before_validate": "ecs_vim.doctype_triggers.buying.supplier.supplier.before_validate",
        "validate": "ecs_vim.doctype_triggers.buying.supplier.supplier.validate",
        "on_update_after_submit": "ecs_vim.doctype_triggers.buying.supplier.supplier.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.buying.supplier.supplier.before_save",
        "on_update": "ecs_vim.doctype_triggers.buying.supplier.supplier.on_update",
    },
    "Supplier Group": {
        "before_insert": "ecs_vim.doctype_triggers.buying.supplier_group.supplier_group.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.buying.supplier_group.supplier_group.after_insert",
        "onload": "ecs_vim.doctype_triggers.buying.supplier_group.supplier_group.onload",
        "before_validate": "ecs_vim.doctype_triggers.buying.supplier_group.supplier_group.before_validate",
        "validate": "ecs_vim.doctype_triggers.buying.supplier_group.supplier_group.validate",
        "on_update_after_submit": "ecs_vim.doctype_triggers.buying.supplier_group.supplier_group.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.buying.supplier_group.supplier_group.before_save",
        "on_update": "ecs_vim.doctype_triggers.buying.supplier_group.supplier_group.on_update",
    },
    "Supplier Quotation": {
        "before_insert": "ecs_vim.doctype_triggers.buying.supplier_quotation.supplier_quotation.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.buying.supplier_quotation.supplier_quotation.after_insert",
        "onload": "ecs_vim.doctype_triggers.buying.supplier_quotation.supplier_quotation.onload",
        "before_validate": "ecs_vim.doctype_triggers.buying.supplier_quotation.supplier_quotation.before_validate",
        "validate": "ecs_vim.doctype_triggers.buying.supplier_quotation.supplier_quotation.validate",
        "on_submit": "ecs_vim.doctype_triggers.buying.supplier_quotation.supplier_quotation.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.buying.supplier_quotation.supplier_quotation.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.buying.supplier_quotation.supplier_quotation.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.buying.supplier_quotation.supplier_quotation.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.buying.supplier_quotation.supplier_quotation.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.buying.supplier_quotation.supplier_quotation.on_update",
    },
    "Address": {
        "before_insert": "ecs_vim.doctype_triggers.crm.address.address.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.crm.address.address.after_insert",
        "onload": "ecs_vim.doctype_triggers.crm.address.address.onload",
        "before_validate": "ecs_vim.doctype_triggers.crm.address.address.before_validate",
        "validate": "ecs_vim.doctype_triggers.crm.address.address.validate",
        "on_update_after_submit": "ecs_vim.doctype_triggers.crm.address.address.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.crm.address.address.before_save",
        "on_update": "ecs_vim.doctype_triggers.crm.address.address.on_update",
    },
    "Contact": {
        "before_insert": "ecs_vim.doctype_triggers.crm.contact.contact.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.crm.contact.contact.after_insert",
        "onload": "ecs_vim.doctype_triggers.crm.contact.contact.onload",
        "before_validate": "ecs_vim.doctype_triggers.crm.contact.contact.before_validate",
        "validate": "ecs_vim.doctype_triggers.crm.contact.contact.validate",
        "on_update_after_submit": "ecs_vim.doctype_triggers.crm.contact.contact.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.crm.contact.contact.before_save",
        "on_update": "ecs_vim.doctype_triggers.crm.contact.contact.on_update",
    },
    "Lead": {
        "before_insert": "ecs_vim.doctype_triggers.crm.lead.lead.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.crm.lead.lead.after_insert",
        "onload": "ecs_vim.doctype_triggers.crm.lead.lead.onload",
        "before_validate": "ecs_vim.doctype_triggers.crm.lead.lead.before_validate",
        "validate": "ecs_vim.doctype_triggers.crm.lead.lead.validate",
        "on_update_after_submit": "ecs_vim.doctype_triggers.crm.lead.lead.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.crm.lead.lead.before_save",
        "on_update": "ecs_vim.doctype_triggers.crm.lead.lead.on_update",
    },
    "Opportunity": {
        "before_insert": "ecs_vim.doctype_triggers.crm.opportunity.opportunity.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.crm.opportunity.opportunity.after_insert",
        "onload": "ecs_vim.doctype_triggers.crm.opportunity.opportunity.onload",
        "before_validate": "ecs_vim.doctype_triggers.crm.opportunity.opportunity.before_validate",
        "validate": "ecs_vim.doctype_triggers.crm.opportunity.opportunity.validate",
        "on_update_after_submit": "ecs_vim.doctype_triggers.crm.opportunity.opportunity.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.crm.opportunity.opportunity.before_save",
        "on_update": "ecs_vim.doctype_triggers.crm.opportunity.opportunity.on_update",
    },
    "Payroll Period": {
        "validate": "ecs_vim.custom_script.payroll_period.payroll_period.validate"
    },
    "Employee": {
        "onload": ["ecs_vim.custom_script.employee.employee.onload"],
        "validate": ["ecs_vim.custom_script.employee.employee.validate"],
        "before_insert": "ecs_vim.doctype_triggers.hr.employee.employee.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.hr.employee.employee.after_insert",
        # "onload": "ecs_vim.doctype_triggers.hr.employee.employee.onload",
        "before_validate": "ecs_vim.doctype_triggers.hr.employee.employee.before_validate",
        # "validate": "ecs_vim.doctype_triggers.hr.employee.employee.validate",
        "on_update_after_submit": "ecs_vim.doctype_triggers.hr.employee.employee.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.hr.employee.employee.before_save",
        "on_update": "ecs_vim.doctype_triggers.hr.employee.employee.on_update",
    },
    "Employee Checkin": {
        "validate": "ecs_vim.custom_script.employee_checkin.employee_checkin.validate",
        "before_insert": "ecs_vim.doctype_triggers.hr.employee_checkin.employee_checkin.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.hr.employee_checkin.employee_checkin.after_insert",
        "onload": "ecs_vim.doctype_triggers.hr.employee_checkin.employee_checkin.onload",
        "before_validate": "ecs_vim.doctype_triggers.hr.employee_checkin.employee_checkin.before_validate",
        # "validate": "ecs_vim.doctype_triggers.hr.employee_checkin.employee_checkin.validate",
        "on_update_after_submit": "ecs_vim.doctype_triggers.hr.employee_checkin.employee_checkin.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.hr.employee_checkin.employee_checkin.before_save",
        "on_update": "ecs_vim.doctype_triggers.hr.employee_checkin.employee_checkin.on_update",
    },
    "Salary Component": {
        "before_insert": "ecs_vim.doctype_triggers.hr.salary_component.salary_component.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.hr.salary_component.salary_component.after_insert",
        "onload": "ecs_vim.doctype_triggers.hr.salary_component.salary_component.onload",
        "before_validate": "ecs_vim.doctype_triggers.hr.salary_component.salary_component.before_validate",
        "validate": "ecs_vim.doctype_triggers.hr.salary_component.salary_component.validate",
        "on_update_after_submit": "ecs_vim.doctype_triggers.hr.salary_component.salary_component.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.hr.salary_component.salary_component.before_save",
        "on_update": "ecs_vim.doctype_triggers.hr.salary_component.salary_component.on_update",
    },
    "Additional Salary": {
        "before_insert": "ecs_vim.doctype_triggers.hr.additional_salary.additional_salary.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.hr.additional_salary.additional_salary.after_insert",
        "onload": "ecs_vim.doctype_triggers.hr.additional_salary.additional_salary.onload",
        "before_validate": "ecs_vim.doctype_triggers.hr.additional_salary.additional_salary.before_validate",
        "validate": "ecs_vim.doctype_triggers.hr.additional_salary.additional_salary.validate",
        "on_submit": "ecs_vim.doctype_triggers.hr.additional_salary.additional_salary.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.hr.additional_salary.additional_salary.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.hr.additional_salary.additional_salary.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.hr.additional_salary.additional_salary.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.hr.additional_salary.additional_salary.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.hr.additional_salary.additional_salary.on_update",
    },
    "Attendance": {
        "validate": "ecs_vim.custom_script.attendance.attendance.validate",
        "on_cancel": "ecs_vim.custom_script.attendance.attendance.on_cancel",
        "after_insert": "ecs_vim.custom_script.attendance.attendance.after_insert",
        # 	"on_submit": ["ecs_vim.custom_script.attendance.attendance.on_submit"],
        # 	"before_cancel": ["ecs_vim.custom_script.attendance.attendance.before_cancel"],
        "on_trash": ["ecs_vim.custom_script.attendance.attendance.on_trash"],
        "before_insert": "ecs_vim.doctype_triggers.hr.attendance.attendance.before_insert",
        # "after_insert": "ecs_vim.doctype_triggers.hr.attendance.attendance.after_insert",
        "onload": "ecs_vim.doctype_triggers.hr.attendance.attendance.onload",
        "before_validate": "ecs_vim.doctype_triggers.hr.attendance.attendance.before_validate",
        # "validate": "ecs_vim.doctype_triggers.hr.attendance.attendance.validate",
        "on_submit": "ecs_vim.doctype_triggers.hr.attendance.attendance.on_submit",
        # "on_cancel": "ecs_vim.doctype_triggers.hr.attendance.attendance.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.hr.attendance.attendance.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.hr.attendance.attendance.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.hr.attendance.attendance.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.hr.attendance.attendance.on_update",
    },
    "Attendance Request": {
        "before_insert": "ecs_vim.doctype_triggers.hr.attendance_request.attendance_request.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.hr.attendance_request.attendance_request.after_insert",
        "onload": "ecs_vim.doctype_triggers.hr.attendance_request.attendance_request.onload",
        "before_validate": "ecs_vim.doctype_triggers.hr.attendance_request.attendance_request.before_validate",
        "validate": "ecs_vim.doctype_triggers.hr.attendance_request.attendance_request.validate",
        "on_submit": "ecs_vim.doctype_triggers.hr.attendance_request.attendance_request.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.hr.attendance_request.attendance_request.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.hr.attendance_request.attendance_request.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.hr.attendance_request.attendance_request.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.hr.attendance_request.attendance_request.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.hr.attendance_request.attendance_request.on_update",
    },
    "Employee Advance": {
        "before_insert": "ecs_vim.doctype_triggers.hr.employee_advance.employee_advance.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.hr.employee_advance.employee_advance.after_insert",
        "onload": "ecs_vim.doctype_triggers.hr.employee_advance.employee_advance.onload",
        "before_validate": "ecs_vim.doctype_triggers.hr.employee_advance.employee_advance.before_validate",
        "validate": "ecs_vim.doctype_triggers.hr.employee_advance.employee_advance.validate",
        "on_submit": "ecs_vim.doctype_triggers.hr.employee_advance.employee_advance.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.hr.employee_advance.employee_advance.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.hr.employee_advance.employee_advance.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.hr.employee_advance.employee_advance.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.hr.employee_advance.employee_advance.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.hr.employee_advance.employee_advance.on_update",
    },
    "Expense Claim": {
        "before_insert": "ecs_vim.doctype_triggers.hr.expense_claim.expense_claim.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.hr.expense_claim.expense_claim.after_insert",
        "onload": "ecs_vim.doctype_triggers.hr.expense_claim.expense_claim.onload",
        "before_validate": "ecs_vim.doctype_triggers.hr.expense_claim.expense_claim.before_validate",
        "validate": "ecs_vim.doctype_triggers.hr.expense_claim.expense_claim.validate",
        "on_submit": "ecs_vim.doctype_triggers.hr.expense_claim.expense_claim.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.hr.expense_claim.expense_claim.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.hr.expense_claim.expense_claim.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.hr.expense_claim.expense_claim.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.hr.expense_claim.expense_claim.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.hr.expense_claim.expense_claim.on_update",
    },
    "Leave Application": {
        "validate": "ecs_vim.custom_script.leave_application.leave_application.validate",
        "before_cancel": "ecs_vim.custom_script.leave_application.leave_application.before_cancel",
        "on_cancel": "ecs_vim.custom_script.leave_application.leave_application.on_cancel",
        "on_trash": "ecs_vim.custom_script.leave_application.leave_application.on_trash",
        "before_save": "ecs_vim.custom_script.leave_application.leave_application.get_user_role",
        # "before_cancel" :"ecs_vim.custom_script.leave_application.leave_application.cancel_wf_doc",
        # "on_trash":"ecs_vim.custom_script.leave_application.leave_application.delete_wf",
        "before_submit": "ecs_vim.custom_script.leave_application.leave_application.get_user_role_validation",
        "before_insert": "ecs_vim.doctype_triggers.hr.leave_application.leave_application.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.hr.leave_application.leave_application.after_insert",
        "onload": "ecs_vim.doctype_triggers.hr.leave_application.leave_application.onload",
        "before_validate": "ecs_vim.doctype_triggers.hr.leave_application.leave_application.before_validate",
        # "validate": "ecs_vim.doctype_triggers.hr.leave_application.leave_application.validate",
        "on_submit": "ecs_vim.doctype_triggers.hr.leave_application.leave_application.on_submit",
        # "on_cancel": "ecs_vim.doctype_triggers.hr.leave_application.leave_application.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.hr.leave_application.leave_application.on_update_after_submit",
        # "before_save": "ecs_vim.doctype_triggers.hr.leave_application.leave_application.before_save",
        # "before_cancel": "ecs_vim.doctype_triggers.hr.leave_application.leave_application.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.hr.leave_application.leave_application.on_update",
    },
    "Loan": {
        "validate": "ecs_vim.custom_script.loan.loan.validate",
        "on_cancel": "ecs_vim.custom_script.loan.loan.on_cancel",
        "on_trash": ["ecs_vim.custom_script.loan.loan.on_trash"],
        "before_insert": "ecs_vim.doctype_triggers.hr.loan.loan.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.hr.loan.loan.after_insert",
        "onload": "ecs_vim.doctype_triggers.hr.loan.loan.onload",
        "before_validate": "ecs_vim.doctype_triggers.hr.loan.loan.before_validate",
        # "validate": "ecs_vim.doctype_triggers.hr.loan.loan.validate",
        "on_submit": "ecs_vim.doctype_triggers.hr.loan.loan.on_submit",
        # "on_cancel": "ecs_vim.doctype_triggers.hr.loan.loan.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.hr.loan.loan.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.hr.loan.loan.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.hr.loan.loan.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.hr.loan.loan.on_update",
    },
    "Loan Application": {
        "validate": "ecs_vim.custom_script.loan_application.loan_application.validate",
        "before_insert": "ecs_vim.doctype_triggers.hr.loan_application.loan_application.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.hr.loan_application.loan_application.after_insert",
        "onload": "ecs_vim.doctype_triggers.hr.loan_application.loan_application.onload",
        "before_validate": "ecs_vim.doctype_triggers.hr.loan_application.loan_application.before_validate",
        # "validate": "ecs_vim.doctype_triggers.hr.loan_application.loan_application.validate",
        "on_submit": "ecs_vim.doctype_triggers.hr.loan_application.loan_application.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.hr.loan_application.loan_application.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.hr.loan_application.loan_application.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.hr.loan_application.loan_application.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.hr.loan_application.loan_application.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.hr.loan_application.loan_application.on_update",
    },
    "Loan Disbursement": {
        "before_insert": "ecs_vim.doctype_triggers.hr.loan_disbursement.loan_disbursement.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.hr.loan_disbursement.loan_disbursement.after_insert",
        "onload": "ecs_vim.doctype_triggers.hr.loan_disbursement.loan_disbursement.onload",
        "before_validate": "ecs_vim.doctype_triggers.hr.loan_disbursement.loan_disbursement.before_validate",
        "validate": "ecs_vim.doctype_triggers.hr.loan_disbursement.loan_disbursement.validate",
        "on_submit": "ecs_vim.doctype_triggers.hr.loan_disbursement.loan_disbursement.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.hr.loan_disbursement.loan_disbursement.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.hr.loan_disbursement.loan_disbursement.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.hr.loan_disbursement.loan_disbursement.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.hr.loan_disbursement.loan_disbursement.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.hr.loan_disbursement.loan_disbursement.on_update",
    },
    "Loan Repayment": {
        "before_insert": "ecs_vim.doctype_triggers.hr.loan_repayment.loan_repayment.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.hr.loan_repayment.loan_repayment.after_insert",
        "onload": "ecs_vim.doctype_triggers.hr.loan_repayment.loan_repayment.onload",
        "before_validate": "ecs_vim.doctype_triggers.hr.loan_repayment.loan_repayment.before_validate",
        "validate": "ecs_vim.doctype_triggers.hr.loan_repayment.loan_repayment.validate",
        "on_submit": "ecs_vim.doctype_triggers.hr.loan_repayment.loan_repayment.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.hr.loan_repayment.loan_repayment.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.hr.loan_repayment.loan_repayment.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.hr.loan_repayment.loan_repayment.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.hr.loan_repayment.loan_repayment.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.hr.loan_repayment.loan_repayment.on_update",
    },
    "Leave Type": {
        "on_change": "ecs_vim.custom_script.leave_type.leave_type.on_change",
        "on_trash": "ecs_vim.custom_script.leave_type.leave_type.on_trash",
    },
    "Loan Type": {
        "validate": "ecs_vim.custom_script.loan_type.loan_type.validate",
        "before_insert": "ecs_vim.doctype_triggers.hr.loan_type.loan_type.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.hr.loan_type.loan_type.after_insert",
        "onload": "ecs_vim.doctype_triggers.hr.loan_type.loan_type.onload",
        "before_validate": "ecs_vim.doctype_triggers.hr.loan_type.loan_type.before_validate",
        # "validate": "ecs_vim.doctype_triggers.hr.loan_type.loan_type.validate",
        "on_submit": "ecs_vim.doctype_triggers.hr.loan_type.loan_type.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.hr.loan_type.loan_type.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.hr.loan_type.loan_type.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.hr.loan_type.loan_type.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.hr.loan_type.loan_type.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.hr.loan_type.loan_type.on_update",
    },
    "Payroll Entry": {
        "before_insert": "ecs_vim.doctype_triggers.hr.payroll_entry.payroll_entry.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.hr.payroll_entry.payroll_entry.after_insert",
        "onload": "ecs_vim.doctype_triggers.hr.payroll_entry.payroll_entry.onload",
        "before_validate": "ecs_vim.doctype_triggers.hr.payroll_entry.payroll_entry.before_validate",
        "validate": "ecs_vim.doctype_triggers.hr.payroll_entry.payroll_entry.validate",
        "on_submit": "ecs_vim.doctype_triggers.hr.payroll_entry.payroll_entry.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.hr.payroll_entry.payroll_entry.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.hr.payroll_entry.payroll_entry.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.hr.payroll_entry.payroll_entry.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.hr.payroll_entry.payroll_entry.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.hr.payroll_entry.payroll_entry.on_update",
    },
    "Salary Slip": {
        "validate": "ecs_vim.custom_script.salary_slip.salary_slip.validate",
        "before_insert": "ecs_vim.doctype_triggers.hr.salary_slip.salary_slip.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.hr.salary_slip.salary_slip.after_insert",
        "onload": "ecs_vim.doctype_triggers.hr.salary_slip.salary_slip.onload",
        "before_validate": "ecs_vim.doctype_triggers.hr.salary_slip.salary_slip.before_validate",
        # "validate": "ecs_vim.doctype_triggers.hr.salary_slip.salary_slip.validate",
        "on_submit": "ecs_vim.doctype_triggers.hr.salary_slip.salary_slip.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.hr.salary_slip.salary_slip.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.hr.salary_slip.salary_slip.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.hr.salary_slip.salary_slip.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.hr.salary_slip.salary_slip.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.hr.salary_slip.salary_slip.on_update",
    },
    "Salary Structure": {
        "before_insert": "ecs_vim.doctype_triggers.hr.salary_structure.salary_structure.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.hr.salary_structure.salary_structure.after_insert",
        "onload": "ecs_vim.doctype_triggers.hr.salary_structure.salary_structure.onload",
        "before_validate": "ecs_vim.doctype_triggers.hr.salary_structure.salary_structure.before_validate",
        "validate": "ecs_vim.doctype_triggers.hr.salary_structure.salary_structure.validate",
        "on_submit": "ecs_vim.doctype_triggers.hr.salary_structure.salary_structure.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.hr.salary_structure.salary_structure.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.hr.salary_structure.salary_structure.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.hr.salary_structure.salary_structure.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.hr.salary_structure.salary_structure.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.hr.salary_structure.salary_structure.on_update",
    },
    "BOM": {
        "before_insert": "ecs_vim.doctype_triggers.manufacturing.bom.bom.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.manufacturing.bom.bom.after_insert",
        "onload": "ecs_vim.doctype_triggers.manufacturing.bom.bom.onload",
        "before_validate": "ecs_vim.doctype_triggers.manufacturing.bom.bom.before_validate",
        "validate": "ecs_vim.doctype_triggers.manufacturing.bom.bom.validate",
        "on_submit": "ecs_vim.doctype_triggers.manufacturing.bom.bom.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.manufacturing.bom.bom.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.manufacturing.bom.bom.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.manufacturing.bom.bom.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.manufacturing.bom.bom.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.manufacturing.bom.bom.on_update",
    },
    "Job Card": {
        "before_insert": "ecs_vim.doctype_triggers.manufacturing.job_card.job_card.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.manufacturing.job_card.job_card.after_insert",
        "onload": "ecs_vim.doctype_triggers.manufacturing.job_card.job_card.onload",
        "before_validate": "ecs_vim.doctype_triggers.manufacturing.job_card.job_card.before_validate",
        "validate": "ecs_vim.doctype_triggers.manufacturing.job_card.job_card.validate",
        "on_submit": "ecs_vim.doctype_triggers.manufacturing.job_card.job_card.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.manufacturing.job_card.job_card.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.manufacturing.job_card.job_card.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.manufacturing.job_card.job_card.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.manufacturing.job_card.job_card.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.manufacturing.job_card.job_card.on_update",
    },
    "Work Order": {
        "before_insert": "ecs_vim.doctype_triggers.manufacturing.work_order.work_order.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.manufacturing.work_order.work_order.after_insert",
        "onload": "ecs_vim.doctype_triggers.manufacturing.work_order.work_order.onload",
        "before_validate": "ecs_vim.doctype_triggers.manufacturing.work_order.work_order.before_validate",
        "validate": "ecs_vim.doctype_triggers.manufacturing.work_order.work_order.validate",
        "on_submit": "ecs_vim.doctype_triggers.manufacturing.work_order.work_order.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.manufacturing.work_order.work_order.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.manufacturing.work_order.work_order.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.manufacturing.work_order.work_order.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.manufacturing.work_order.work_order.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.manufacturing.work_order.work_order.on_update",
    },
    "Project": {
        "before_insert": "ecs_vim.doctype_triggers.projects.project.project.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.projects.project.project.after_insert",
        "onload": "ecs_vim.doctype_triggers.projects.project.project.onload",
        "before_validate": "ecs_vim.doctype_triggers.projects.project.project.before_validate",
        "validate": "ecs_vim.doctype_triggers.projects.project.project.validate",
        "before_save": "ecs_vim.doctype_triggers.projects.project.project.before_save",
        "on_update": "ecs_vim.doctype_triggers.projects.project.project.on_update",
    },
    "Task": {
        "before_insert": "ecs_vim.doctype_triggers.projects.task.task.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.projects.task.task.after_insert",
        "onload": "ecs_vim.doctype_triggers.projects.task.task.onload",
        "before_validate": "ecs_vim.doctype_triggers.projects.task.task.before_validate",
        "validate": "ecs_vim.doctype_triggers.projects.task.task.validate",
        "before_save": "ecs_vim.doctype_triggers.projects.task.task.before_save",
        "on_update": "ecs_vim.doctype_triggers.projects.task.task.on_update",
    },
    "Timesheet": {
        "on_submit": "ecs_vim.custom_script.timesheet.timesheet.on_submit",
        # "on_submit": "ecs_vim.custom_script.timesheet.timesheet.create_attendance"
        "on_cancel": "ecs_vim.custom_script.timesheet.timesheet.on_cancel",
        "validate": "ecs_vim.custom_script.timesheet.timesheet.validate",
        "before_save": "ecs_vim.custom_script.timesheet.timesheet.before_save",
        "before_insert": "ecs_vim.doctype_triggers.projects.timesheet.timesheet.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.projects.timesheet.timesheet.after_insert",
        "onload": "ecs_vim.doctype_triggers.projects.timesheet.timesheet.onload",
        "before_validate": "ecs_vim.doctype_triggers.projects.timesheet.timesheet.before_validate",
        # "validate": "ecs_vim.doctype_triggers.projects.timesheet.timesheet.validate",
        # "before_save": "ecs_vim.doctype_triggers.projects.timesheet.timesheet.before_save",
        "on_update": "ecs_vim.doctype_triggers.projects.timesheet.timesheet.on_update",
    },
    "Customer": {
        "validate": "ecs_vim.doctype_triggers.customer.customer.validate",
        "on_update": "ecs_vim.doctype_triggers.selling.customer.customer.reset_syncedflag",
    },
    "Customer Group": {
        "before_insert": "ecs_vim.doctype_triggers.selling.customer_group.customer_group.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.selling.customer_group.customer_group.after_insert",
        "onload": "ecs_vim.doctype_triggers.selling.customer_group.customer_group.onload",
        "before_validate": "ecs_vim.doctype_triggers.selling.customer_group.customer_group.before_validate",
        "validate": "ecs_vim.doctype_triggers.selling.customer_group.customer_group.validate",
        "before_save": "ecs_vim.doctype_triggers.selling.customer_group.customer_group.before_save",
        "on_update": "ecs_vim.doctype_triggers.selling.customer_group.customer_group.on_update",
    },
    "Pricing Rule": {
        "before_insert": "ecs_vim.doctype_triggers.selling.pricing_rule.pricing_rule.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.selling.pricing_rule.pricing_rule.after_insert",
        "onload": "ecs_vim.doctype_triggers.selling.pricing_rule.pricing_rule.onload",
        "before_validate": "ecs_vim.doctype_triggers.selling.pricing_rule.pricing_rule.before_validate",
        "validate": "ecs_vim.doctype_triggers.selling.pricing_rule.pricing_rule.validate",
        "before_save": "ecs_vim.doctype_triggers.selling.pricing_rule.pricing_rule.before_save",
        "on_update": "ecs_vim.doctype_triggers.selling.pricing_rule.pricing_rule.on_update",
    },
    "Sales Partner": {
        "before_insert": "ecs_vim.doctype_triggers.selling.sales_partner.sales_partner.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.selling.sales_partner.sales_partner.after_insert",
        "onload": "ecs_vim.doctype_triggers.selling.sales_partner.sales_partner.onload",
        "before_validate": "ecs_vim.doctype_triggers.selling.sales_partner.sales_partner.before_validate",
        "validate": "ecs_vim.doctype_triggers.selling.sales_partner.sales_partner.validate",
        "before_save": "ecs_vim.doctype_triggers.selling.sales_partner.sales_partner.before_save",
        "on_update": "ecs_vim.doctype_triggers.selling.sales_partner.sales_partner.on_update",
    },
    "Sales Person": {
        "before_insert": "ecs_vim.doctype_triggers.selling.sales_person.sales_person.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.selling.sales_person.sales_person.after_insert",
        "onload": "ecs_vim.doctype_triggers.selling.sales_person.sales_person.onload",
        "before_validate": "ecs_vim.doctype_triggers.selling.sales_person.sales_person.before_validate",
        "validate": "ecs_vim.doctype_triggers.selling.sales_person.sales_person.validate",
        "before_save": "ecs_vim.doctype_triggers.selling.sales_person.sales_person.before_save",
        "on_update": "ecs_vim.doctype_triggers.selling.sales_person.sales_person.on_update",
    },
    "Quotation": {
        "before_insert": "ecs_vim.doctype_triggers.selling.quotation.quotation.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.selling.quotation.quotation.after_insert",
        "onload": "ecs_vim.doctype_triggers.selling.quotation.quotation.onload",
        "before_validate": "ecs_vim.doctype_triggers.selling.quotation.quotation.before_validate",
        "validate": "ecs_vim.doctype_triggers.selling.quotation.quotation.validate",
        "on_submit": "ecs_vim.doctype_triggers.selling.quotation.quotation.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.selling.quotation.quotation.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.selling.quotation.quotation.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.selling.quotation.quotation.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.selling.quotation.quotation.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.selling.quotation.quotation.on_update",
    },
    "Sales Order": {
        "before_submit": "ecs_vim.doctype_triggers.selling.sales_order.sales_order.before_submit",
        "before_insert": "ecs_vim.doctype_triggers.selling.sales_order.sales_order.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.selling.sales_order.sales_order.after_insert",
        "onload": "ecs_vim.doctype_triggers.selling.sales_order.sales_order.onload",
        "before_validate": "ecs_vim.doctype_triggers.selling.sales_order.sales_order.before_validate",
        "validate": "ecs_vim.doctype_triggers.selling.sales_order.sales_order.validate",
        "on_submit": "ecs_vim.invoice_billing.onSumbmitinvoiceSync",
        "on_cancel": "ecs_vim.doctype_triggers.selling.sales_order.sales_order.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.selling.sales_order.sales_order.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.selling.sales_order.sales_order.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.selling.sales_order.sales_order.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.selling.sales_order.sales_order.on_update",
    },
    "Delivery Note": {
        "before_insert": "ecs_vim.doctype_triggers.stock.delivery_note.delivery_note.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.stock.delivery_note.delivery_note.after_insert",
        "onload": "ecs_vim.doctype_triggers.stock.delivery_note.delivery_note.onload",
        "before_validate": "ecs_vim.doctype_triggers.stock.delivery_note.delivery_note.before_validate",
        "validate": "ecs_vim.doctype_triggers.stock.delivery_note.delivery_note.validate",
        "on_submit": "ecs_vim.doctype_triggers.stock.delivery_note.delivery_note.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.stock.delivery_note.delivery_note.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.stock.delivery_note.delivery_note.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.stock.delivery_note.delivery_note.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.stock.delivery_note.delivery_note.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.stock.delivery_note.delivery_note.on_update",
    },
    "Purchase Receipt": {
        "before_insert": "ecs_vim.doctype_triggers.stock.purchase_receipt.purchase_receipt.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.stock.purchase_receipt.purchase_receipt.after_insert",
        "onload": "ecs_vim.doctype_triggers.stock.purchase_receipt.purchase_receipt.onload",
        "before_validate": "ecs_vim.doctype_triggers.stock.purchase_receipt.purchase_receipt.before_validate",
        "validate": "ecs_vim.doctype_triggers.stock.purchase_receipt.purchase_receipt.validate",
        "on_submit": "ecs_vim.doctype_triggers.stock.purchase_receipt.purchase_receipt.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.stock.purchase_receipt.purchase_receipt.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.stock.purchase_receipt.purchase_receipt.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.stock.purchase_receipt.purchase_receipt.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.stock.purchase_receipt.purchase_receipt.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.stock.purchase_receipt.purchase_receipt.on_update",
    },
    "Stock Entry": {
        "before_insert": "ecs_vim.doctype_triggers.stock.stock_entry.stock_entry.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.stock.stock_entry.stock_entry.after_insert",
        "onload": "ecs_vim.doctype_triggers.stock.stock_entry.stock_entry.onload",
        "before_validate": "ecs_vim.doctype_triggers.stock.stock_entry.stock_entry.before_validate",
        "validate": "ecs_vim.doctype_triggers.stock.stock_entry.stock_entry.validate",
        "on_submit": "ecs_vim.doctype_triggers.stock.stock_entry.stock_entry.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.stock.stock_entry.stock_entry.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.stock.stock_entry.stock_entry.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.stock.stock_entry.stock_entry.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.stock.stock_entry.stock_entry.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.stock.stock_entry.stock_entry.on_update",
    },
    "Stock Reconciliation": {
        "before_insert": "ecs_vim.doctype_triggers.stock.stock_reconciliation.stock_reconciliation.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.stock.stock_reconciliation.stock_reconciliation.after_insert",
        "onload": "ecs_vim.doctype_triggers.stock.stock_reconciliation.stock_reconciliation.onload",
        "before_validate": "ecs_vim.doctype_triggers.stock.stock_reconciliation.stock_reconciliation.before_validate",
        "validate": "ecs_vim.doctype_triggers.stock.stock_reconciliation.stock_reconciliation.validate",
        "on_submit": "ecs_vim.doctype_triggers.stock.stock_reconciliation.stock_reconciliation.on_submit",
        "on_cancel": "ecs_vim.doctype_triggers.stock.stock_reconciliation.stock_reconciliation.on_cancel",
        "on_update_after_submit": "ecs_vim.doctype_triggers.stock.stock_reconciliation.stock_reconciliation.on_update_after_submit",
        "before_save": "ecs_vim.doctype_triggers.stock.stock_reconciliation.stock_reconciliation.before_save",
        "before_cancel": "ecs_vim.doctype_triggers.stock.stock_reconciliation.stock_reconciliation.before_cancel",
        "on_update": "ecs_vim.doctype_triggers.stock.stock_reconciliation.stock_reconciliation.on_update",
    },
    "Item": {
        "before_insert": "ecs_vim.doctype_triggers.stock.item.item.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.stock.item.item.after_insert",
        "onload": "ecs_vim.doctype_triggers.stock.item.item.onload",
        "before_validate": "ecs_vim.doctype_triggers.stock.item.item.before_validate",
        "validate": "ecs_vim.doctype_triggers.stock.item.item.validate",
        "before_save": "ecs_vim.doctype_triggers.stock.item.item.before_save",
        "on_update": "ecs_vim.doctype_triggers.stock.item.item.on_update",
    },
    "Item Group": {
        "before_insert": "ecs_vim.doctype_triggers.stock.item_group.item_group.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.stock.item_group.item_group.after_insert",
        "onload": "ecs_vim.doctype_triggers.stock.item_group.item_group.onload",
        "before_validate": "ecs_vim.doctype_triggers.stock.item_group.item_group.before_validate",
        "validate": "ecs_vim.doctype_triggers.stock.item_group.item_group.validate",
        "before_save": "ecs_vim.doctype_triggers.stock.item_group.item_group.before_save",
        "on_update": "ecs_vim.doctype_triggers.stock.item_group.item_group.on_update",
    },
    "Item Price": {
        "before_insert": "ecs_vim.doctype_triggers.stock.item_price.item_price.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.stock.item_price.item_price.after_insert",
        "onload": "ecs_vim.doctype_triggers.stock.item_price.item_price.onload",
        "before_validate": "ecs_vim.doctype_triggers.stock.item_price.item_price.before_validate",
        "validate": "ecs_vim.doctype_triggers.stock.item_price.item_price.validate",
        "before_save": "ecs_vim.doctype_triggers.stock.item_price.item_price.before_save",
        "on_update": "ecs_vim.doctype_triggers.stock.item_price.item_price.on_update",
    },
    "Website Item": {
        "before_insert": "ecs_vim.doctype_triggers.stock.website_item.website_item.before_insert",
        "after_insert": "ecs_vim.doctype_triggers.stock.website_item.website_item.after_insert",
        "onload": "ecs_vim.doctype_triggers.stock.website_item.website_item.onload",
        "before_validate": "ecs_vim.doctype_triggers.stock.website_item.website_item.before_validate",
        "validate": "ecs_vim.doctype_triggers.stock.website_item.website_item.validate",
        "before_save": "ecs_vim.doctype_triggers.stock.website_item.website_item.before_save",
        "on_update": "ecs_vim.doctype_triggers.stock.website_item.website_item.on_update",
    },
    "POS Invoice": {
        "on_submit": "ecs_vim.doctype_triggers.pos_invoice.pos_invoice.on_submit",
        "before_cancel": "ecs_vim.doctype_triggers.pos_invoice.pos_invoice.on_cancel",
        "validate": "ecs_vim.doctype_triggers.pos_invoice.pos_invoice.validate",
    },
    "Coupon Code": {
        "validate": "ecs_vim.doctype_triggers.coupon_code.coupon_code.validate",
    },
}
doctype_js = {
    "Asset": "doctype_triggers/asset/asset.js",
    "Journal Entry": "doctype_triggers/accounting/journal_entry/journal_entry.js",
    "Payment Entry": "doctype_triggers/accounting/payment_entry/payment_entry.js",
    "Purchase Invoice": "doctype_triggers/accounting/purchase_invoice/purchase_invoice.js",
    "Sales Invoice": "doctype_triggers/accounting/sales_invoice/sales_invoice.js",
    "Material Request": "doctype_triggers/buying/material_request/material_request.js",
    "Purchase Oder": "doctype_triggers/buying/purchase_order/purchase_order.js",
    "Request For Quotation": "doctype_triggers/buying/request_for_quotation/request_for_quotation.js",
    "Supplier": "doctype_triggers/buying/supplier/supplier.js",
    "Supplier Group": "doctype_triggers/buying/supplier_group/supplier_group.js",
    "Supplier Quotation": "doctype_triggers/buying/supplier_quotation/supplier_quotation.js",
    "Address": "doctype_triggers/crm/address/address.js",
    "Contact": "doctype_triggers/crm/contact/contact.js",
    "Lead": "doctype_triggers/crm/lead/lead.js",
    "Oppurtunity": "doctype_triggers/crm/oppurtunity/oppurtunity.js",
    ##
    "Employee": ["custom_script/employee/employee.js"],
    "Company": ["custom_script/company/company.js"],
    "Attendance": ["custom_script/attendance/attendance.js"],
    "Salary Slip": ["custom_script/salary_slip/salary_slip.js"],
    "Leave Application": "custom_script/leave_application/leave_application.js",
    "Payroll Entry": "custom_script/payroll_entry/payroll_entry.js",
    "Designation": "custom_script/designation/designation.js",
    "Holiday List": "custom_script/holiday_list/holiday_list.js",
    "Loan Application": "custom_script/loan_application/loan_application.js",
    "Shift Request": "custom_script/shift_request/shift_request.js",
    "Shift Type": "custom_script/shift_type/shift_type.js",
    "Timesheet": "custom_script/timesheet/timesheet.js",
    "Loan": "custom_script/Loan/Loan.js",
    # "Employee": "doctype_triggers/hr/employee/employee.js",
    "Employee Checkin": "doctype_triggers/hr/employee_checkin/employee_checkin.js",
    "Salary Component": "doctype_triggers/hr/salary_component/salary_component.js",
    "Additional Salary": "doctype_triggers/hr/additional_salary/additional_salary.js",
    # "Attendance": "doctype_triggers/hr/attendance/attendance.js",
    "Attendance Request": "doctype_triggers/hr/attendance_request/attendance_request.js",
    "Employee Advance": "doctype_triggers/hr/employee_advance/employee_advance.js",
    "Expense Claim": "doctype_triggers/hr/expense_claim/expense_claim.js",
    # "Leave Application": "doctype_triggers/hr/leave_application/leave_application.js",
    # "Loan": "doctype_triggers/hr/loan/loan.js",
    # "Loan Application": "doctype_triggers/hr/loan_application/loan_application.js",
    "Loan Disbursement": "doctype_triggers/hr/loan_disbursement/loan_disbursement.js",
    "Loan Repayment": "doctype_triggers/hr/loan_repayment/loan_repayment.js",
    "Loan Type": "doctype_triggers/hr/loan_type/loan_type.js",
    # "Payroll Entry": "doctype_triggers/hr/payroll_entry/payroll_entry.js",
    # "Salary Slip": "doctype_triggers/hr/salary_slip/salary_slip.js",
    "Salary Structure": "doctype_triggers/hr/salary_structure/salary_structure.js",
    "BOM": "doctype_triggers/manufacturing/bom/bom.js",
    "Job Card": "doctype_triggers/manufacturing/job_card/job_card.js",
    "Work Order": "doctype_triggers/manufacturing/work_order/work_order.js",
    "Project": "doctype_triggers/projects/project/project.js",
    "Task": "doctype_triggers/projects/task/task.js",
    # "Timesheet": "doctype_triggers/projects/timesheet/timesheet.js",
    "Customer": "doctype_triggers/selling/customer/customer.js",
    "Customer Group": "doctype_triggers/selling/customer_group/customer_group.js",
    "Pricing Rule": "doctype_triggers/selling/pricing_rule/pricing_rule.js",
    "Sales Partner": "doctype_triggers/selling/sales_partner/sales_partner.js",
    "Sales Person": "doctype_triggers/selling/sales_person/sales_person.js",
    "Quotation": "doctype_triggers/selling/quotation/quotation.js",
    "Sales Order": "doctype_triggers/selling/sales_order/sales_order.js",
    "Delivery Note": "doctype_triggers/stock/delivery_note/delivery_note.js",
    "Purchase Receipt": "doctype_triggers/stock/purchase_receipt/purchase_receipt.js",
    "Stock Entry": "doctype_triggers/stock/stock_entry/stock_entry.js",
    "Stock Reconciliation": "doctype_triggers/stock/stock_reconciliation/stock_reconciliation.js",
    "Item": "doctype_triggers/stock/item/item.js",
    "Item Group": "doctype_triggers/stock/item_group/item_group.js",
    "Item Price": "doctype_triggers/stock/item_price/item_price.js",
    "Website Item": "doctype_triggers/stock/website_item/website_item.js",
    "POS Invoice": "doctype_triggers/pos_invoice/pos_invoice.js",
    "POS Opening Entry": "doctype_triggers/pos_opeing_entry/pos_opening_entry.js",
    "POS Closing Entry": "doctype_triggers/pos_closing_entry/pos_closing_entry.js",
    "Purchase Order": "doctype_triggers/purchase_order/purchase_order.js",
    "Selling Settings": "doctype_triggers/selling_settings/selling_settings.js",
    "Product Bundle": "doctype_triggers/product_bundle/product_bundle.js",
    "Repost Item Valuation": "doctype_triggers/repost_item_valuation/repost_item_valuation.js",
    "Coupon Code": "doctype_triggers/coupon_code/coupon_code.js",
    "Promotional Scheme": "doctype_triggers/promotional_scheme/promotional_scheme.js",
}


# app_include_css = "/assets/app_name/css/ecs.css"
# app_include_js = "/assets/app_name/js/ecs.js"
# web_include_js = "/assets/js/web_ecs.min.js"
# web_include_css = "/assets/js/web_ecs.min.css"


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/app_name/css/app_name.css"
# app_include_js = "/assets/app_name/js/app_name.js"

# include js, css files in header of web template
# web_include_css = "/assets/app_name/css/app_name.css"
# web_include_js = "/assets/app_name/js/app_name.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "app_name/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}

doctype_list_js = {
    "Loan Application": "custom_script/loan_application/loan_application_list.js",
    "Attendance": "custom_script/attendance/attendance_list.js",
}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ecs_vim.install.before_install"
# after_install = "ecs_vim.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ecs_vim.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
    "POS Invoice": "ecs_vim.doctype_triggers.pos_invoice.pos_invoice.CustomPOSInvoice",
    "Item": "ecs_vim.doctype_triggers.item.item.CustomItem",
    "Communication": "ecs_vim.doctype_triggers.communication.email.Customemail",
    "Payment Entry": "ecs_vim.doctype_triggers.payment_entry.payment_entry.CustomPaymentEntry",
    "Shift Assignment": "ecs_vim.custom_script.shift_assignment.shift_assignment.CustomShiftAssignment",
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
    "cron": {
        # Sync data to salesforce every 5 minutes
        "*/5 * * * *": [
            # "ecs_vim.api.send_renew_sms",
            "ecs_vim.ecs_vim.doctype.salesforce_integration.salesforce_integration.syncCustomer",
            "ecs_vim.ecs_vim.doctype.salesforce_integration.salesforce_integration.syncCustomerFamily",
            "ecs_vim.ecs_vim.doctype.salesforce_integration.salesforce_integration.syncOrders",
            "ecs_vim.ecs_vim.doctype.salesforce_integration.salesforce_integration.syncInvoices",
            "ecs_vim.ecs_vim.doctype.salesforce_integration.salesforce_integration.syncItems",
            "ecs_vim.ecs_vim.doctype.salesforce_integration.salesforce_integration.updateItems",
        ]
    },
    "monthly_long": ["ecs_vim.doctype_triggers.employee.employee.generate_coupon"],
    "daily": [
        "ecs_vim.ecs_vim.doctype.biostar_settings.biostar_settings.syn_attendance",
        "ecs_vim.ecs_vim.doctype.workflow_delegation.workflow_delegation.assign_delegated_role",
    ],
    "hourly": [
        "ecs_vim.custom_script.attendance.holiday_attendance.holiday_attendance"
    ],
}
# Testing
# -------

# before_tests = "ecs_vim.install.before_tests"

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
    "erpnext.e_commerce.product_info.get_product_info_for_website": "ecs_vim.api.get_product_info_for_website",
    "erpnext.e_commerce.shopping_cart.update_cart": "ecs_vim.api.update_cart",
    "erpnext.e_commerce.shopping_cart.place_order": "ecs_vim.api.place_order",
    "erpnext.selling.doctype.sales_order.sales_order.make_work_orders": "ecs_vim.doctype_triggers.selling.sales_order.sales_order.make_work_orders",
    "frappe.core.doctype.user.user.sign_up": "ecs_vim.api.sign_up",
    "frappe.core.doctype.user.user.update_password": "ecs_vim.api.update_password",
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ecs_vim.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
    {
        "doctype": "{doctype_1}",
        "filter_by": "{filter_by}",
        "redact_fields": ["{field_1}", "{field_2}"],
        "partial": 1,
    },
    {
        "doctype": "{doctype_2}",
        "filter_by": "{filter_by}",
        "partial": 1,
    },
    {
        "doctype": "{doctype_3}",
        "strict": False,
    },
    {"doctype": "{doctype_4}"},
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"ecs_vim.auth.validate"
# ]

import erpnext.selling.doctype.customer.customer as _erp_customer
import ecs_vim.doctype_triggers.customer.customer as _vim_customer

_erp_customer.make_contact = _vim_customer.make_contact


import erpnext.controllers.queries as _erp_itemqry
import ecs_vim.doctype_triggers.stock.stock_entry.stock_entry as _vim_itemqry

_erp_itemqry.item_query = _vim_itemqry.item_query

import erpnext.portal.utils as _erp_utils
import ecs_vim.api as _vim_api

_erp_utils.party_exists = _vim_api.party_exists


import frappe.core.doctype.user.user as _erp_user

_erp_user.create_contact = _vim_api.create_contact

_erp_user.create_party_contact = _vim_api.create_party_contact

_erp_user.create_customer_or_supplier = _vim_api.create_customer_or_supplier

from frappe.core.doctype.user.user import User

User.reset_password = _vim_api.reset_password
