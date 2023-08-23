from __future__ import unicode_literals
from ast import If
from xxlimited import new
import frappe
from frappe.utils import flt
from frappe import msgprint, _
from frappe.model.meta import get_field_precision
from erpnext.accounts.doctype.accounting_dimension.accounting_dimension import get_accounting_dimensions, get_dimension_with_children
import datetime as dt
from datetime import datetime
import collections, functools, operator
def execute(filters=None):
	return _execute(filters)

def _execute(filters, additional_table_columns=None, additional_query_columns=None):
	if not filters: filters = frappe._dict({})
	fromdate=datetime.combine(datetime.strptime(str(filters.from_date), '%Y-%m-%d'), datetime.strptime(str(filters.posting_time),"%H:%M:%S").time())
	todate=datetime.combine(datetime.strptime(str(filters.to_date), '%Y-%m-%d'), datetime.strptime(str(filters.posting_timeto),"%H:%M:%S").time())
	filters["fromdate"] = fromdate
	filters["todate"] = todate
	
	invoice_list = get_invoices(filters, additional_query_columns)
	columns, income_accounts, tax_accounts, unrealized_profit_loss_accounts = get_columns(invoice_list, additional_table_columns)

	if not invoice_list:
		msgprint(_("No record found"))
		return columns, invoice_list

	invoice_income_map = get_invoice_income_map(invoice_list)
	internal_invoice_map = get_internal_invoice_map(invoice_list)
	invoice_income_map, invoice_tax_map = get_invoice_tax_map(invoice_list,
	invoice_income_map, income_accounts)
	#Cost Center & Warehouse Map
	invoice_cc_wh_map = get_invoice_cc_wh_map(invoice_list)
	invoice_so_dn_map = get_invoice_so_dn_map(invoice_list)
	company_currency = frappe.get_cached_value('Company',  filters.get("company"),  "default_currency")
	mode_of_payments = get_mode_of_payments([inv.name for inv in invoice_list])
	
	invoice_cc_wh_map_group= get_invoice_cc_wh_map_group(invoice_list)
	 
	group_data = []
	data = []
	for inv in invoice_list:
		# invoice details
		sales_order = list(set(invoice_so_dn_map.get(inv.name, {}).get("sales_order", [])))
		delivery_note = list(set(invoice_so_dn_map.get(inv.name, {}).get("delivery_note", [])))
		cost_center = list(set(invoice_cc_wh_map.get(inv.name, {}).get("cost_center", [])))
		warehouse = list(set(invoice_cc_wh_map.get(inv.name, {}).get("warehouse", [])))

		row = {
			'invoice': inv.name
		}

		if additional_query_columns:
			for col in additional_query_columns:
				row.update({
					col: inv.get(col)
				})

		row.update({
			
			'cost_center': ", ".join(cost_center)
		})

		# map income values
		base_net_total = 0
		for income_acc in income_accounts:
			if inv.is_internal_customer and inv.company == inv.represents_company:
				income_amount = 0
			else:
				income_amount = flt(invoice_income_map.get(inv.name, {}).get(income_acc))

			base_net_total += income_amount
			row.update({
				frappe.scrub(income_acc): income_amount
			})

		# Add amount in unrealized account
		for account in unrealized_profit_loss_accounts:
			row.update({
				frappe.scrub(account): flt(internal_invoice_map.get((inv.name, account)))
			})

		# net total
		row.update({'net_total': base_net_total or inv.base_net_total})

		# tax account
		total_tax = 0
		for tax_acc in tax_accounts:
			if tax_acc not in income_accounts:
				
				tax_amount_precision = get_field_precision(frappe.get_meta("Sales Taxes and Charges").get_field("tax_amount"), currency=company_currency) or 2
				tax_amount = flt(invoice_tax_map.get(inv.name, {}).get(tax_acc), tax_amount_precision)
				total_tax += tax_amount
				row.update({
					frappe.scrub(tax_acc): tax_amount
				})

		# total tax, grand total, outstanding amount & rounded total

		row.update({
			'tax_total': total_tax,
			'grand_total': inv.base_grand_total,
			'rounded_total': inv.base_rounded_total,
			'outstanding_amount': inv.outstanding_amount
		})

		data.append(row)
		frappe.errprint(data)
	cost_center = list(set(invoice_cc_wh_map_group.get("cost_center", [])))					
	for x in cost_center:
			row = {
				}
			row.update({
					"cost_center": x
				})	
			base_net_total = 0
			# map income values	
			new_list = [el for el in data if el["cost_center"]==x]
			
			for income_acc in income_accounts:
					result=sum([row[str(frappe.scrub(income_acc))] for row in new_list])
					
					base_net_total+=result
					row.update({
						frappe.scrub(income_acc): result
						})
					
			# Add amount in unrealized account
			
			for account in unrealized_profit_loss_accounts:
				for dict_item in data:
						for key,value in dict_item.items():
								if frappe.scrub(account)==key and dict_item['cost_center']==x:
									row.update({
											frappe.scrub(account): account
										})		
			row.update({'net_total': base_net_total})
			total_tax = 0
			for tax_acc in tax_accounts:
				if tax_acc not in income_accounts:
						frappe.errprint(frappe.scrub(tax_acc))
						result_t=sum([row[str(frappe.scrub(tax_acc))] for row in new_list])
						frappe.errprint([frappe.scrub(tax_acc),result_t])
						total_tax += result_t
						row.update({
							frappe.scrub(tax_acc): result_t
						})

			# total tax, grand total, outstanding amount & rounded total
			base_rounded_total=0;base_grand_total=0;outstanding_amount=0
			base_rounded_total=sum([row['rounded_total'] for row in new_list])
			base_grand_total=sum([row['grand_total'] for row in new_list])
			outstanding_amount=sum([row['outstanding_amount'] for row in new_list])
			
			row.update({
				'tax_total': total_tax,
				'grand_total': base_grand_total,
				'rounded_total': base_rounded_total,
				'outstanding_amount': outstanding_amount
			})
			group_data.append(row)
		
		
   
	return columns, group_data

def get_columns(invoice_list, additional_table_columns):
	"""return columns based on filters"""
	columns = [
		
	]

	if additional_table_columns:
		columns += additional_table_columns

	columns +=[
		
		{
			'label': _("Cost Center"),
			'fieldname': 'cost_center',
			'fieldtype': 'Link',
			'options': 'Cost Center',
			'width': 100
		},
		
	]

	income_accounts = []
	tax_accounts = []
	income_columns = []
	tax_columns = []
	unrealized_profit_loss_accounts = []
	unrealized_profit_loss_account_columns = []

	if invoice_list:
		income_accounts = frappe.db.sql_list("""select distinct income_account
			from `tabSales Invoice Item` where docstatus = 1 and parent in (%s)
			order by income_account""" %
			', '.join(['%s']*len(invoice_list)), tuple([inv.name for inv in invoice_list]))

		tax_accounts = 	frappe.db.sql_list("""select distinct account_head
			from `tabSales Taxes and Charges` where parenttype = 'Sales Invoice'
			and docstatus = 1 and base_tax_amount_after_discount_amount != 0
			and parent in (%s) order by account_head""" %
			', '.join(['%s']*len(invoice_list)), tuple([inv.name for inv in invoice_list]))

		unrealized_profit_loss_accounts = frappe.db.sql_list("""SELECT distinct unrealized_profit_loss_account
			from `tabSales Invoice` where docstatus = 1 and name in (%s)
			and ifnull(unrealized_profit_loss_account, '') != ''
			order by unrealized_profit_loss_account""" %
			', '.join(['%s']*len(invoice_list)), tuple([inv.name for inv in invoice_list]))

	for account in income_accounts:
		
		income_columns.append({
			"label": account,
			"fieldname": frappe.scrub(account),
			"fieldtype": "Currency",
			"options": "currency",
			"width": 120
		})

	for account in tax_accounts:
		if account not in income_accounts:
			tax_columns.append({
				"label": account,
				"fieldname": frappe.scrub(account),
				"fieldtype": "Currency",
				"options": "currency",
				"width": 120
			})

	for account in unrealized_profit_loss_accounts:
		unrealized_profit_loss_account_columns.append({
			"label": account,
			"fieldname": frappe.scrub(account),
			"fieldtype": "Currency",
			"options": "currency",
			"width": 120
		})

	net_total_column = [{
		"label": _("Net Total"),
		"fieldname": "net_total",
		"fieldtype": "Currency",
		"options": "currency",
		"width": 120
	}]

	total_columns = [
		{
			"label": _("Tax Total"),
			"fieldname": "tax_total",
			"fieldtype": "Currency",
			"options": 'currency',
			"width": 120
		},
		{
			"label": _("Grand Total"),
			"fieldname": "grand_total",
			"fieldtype": "Currency",
			"options": 'currency',
			"width": 120
		},
		
	]

	columns = columns + income_columns + unrealized_profit_loss_account_columns + \
		net_total_column + tax_columns + total_columns

	return columns, income_accounts, tax_accounts, unrealized_profit_loss_accounts

def get_conditions(filters):
	conditions = ""

	if filters.get("company"): conditions += " and company=%(company)s"
	
	if filters.get("from_date"): conditions += " and posting_date >= %(from_date)s"
	if filters.get("to_date"): conditions += " and posting_date <= %(to_date)s"
	if filters.get("posting_time"):conditions+=" and creation >= %(fromdate)s"
	if filters.get("posting_timeto"):conditions+=" and creation <= %(todate)s"
	

	if filters.get("cost_center"):
		conditions +=  """ and exists(select name from `tabPOS Invoice Item`
			 where parent=`tabPOS Invoice`.name
				 and ifnull(`tabPOS Invoice Item`.cost_center, '') = %(cost_center)s)"""

	accounting_dimensions = get_accounting_dimensions(as_list=False)

	if accounting_dimensions:
		common_condition = """
			and exists(select name from `tabSales Invoice Item`
				where parent=`tabSales Invoice`.name
			"""
		for dimension in accounting_dimensions:
			if filters.get(dimension.fieldname):
				if frappe.get_cached_value('DocType', dimension.document_type, 'is_tree'):
					filters[dimension.fieldname] = get_dimension_with_children(dimension.document_type,
						filters.get(dimension.fieldname))

					conditions += common_condition + "and ifnull(`tabSales Invoice Item`.{0}, '') in %({0})s)".format(dimension.fieldname)
				else:
					conditions += common_condition + "and ifnull(`tabSales Invoice Item`.{0}, '') in (%({0})s))".format(dimension.fieldname)
	
	return conditions

def get_invoices(filters, additional_query_columns):
	if additional_query_columns:
		additional_query_columns = ', ' + ', '.join(additional_query_columns)

	conditions = get_conditions(filters)
	
	return frappe.db.sql("""
		select name,  debit_to, project, customer,
		customer_name, owner, remarks, territory, tax_id, customer_group,
		base_net_total, base_grand_total, base_rounded_total, outstanding_amount,
		is_internal_customer, represents_company, company {0}
		from `tabSales Invoice`
		inner join(select distinct consolidated_invoice from `tabPOS Invoice` where docstatus=1 %s) PI on PI.consolidated_invoice=`tabSales Invoice`.name
		where docstatus = 1  order by  name desc""".format(additional_query_columns or '') %
		conditions, filters, as_dict=1)


def get_invoice_income_map(invoice_list):
	income_details = frappe.db.sql("""select parent, income_account, sum(base_net_amount) as amount
		from `tabSales Invoice Item` where parent in (%s) group by parent, income_account""" %
		', '.join(['%s']*len(invoice_list)), tuple([inv.name for inv in invoice_list]), as_dict=1)

	invoice_income_map = {}
	for d in income_details:
		invoice_income_map.setdefault(d.parent, frappe._dict()).setdefault(d.income_account, [])
		invoice_income_map[d.parent][d.income_account] = flt(d.amount)

	return invoice_income_map

def get_internal_invoice_map(invoice_list):
	unrealized_amount_details = frappe.db.sql("""SELECT name, unrealized_profit_loss_account,
		base_net_total as amount from `tabSales Invoice` where name in (%s)
		and is_internal_customer = 1 and company = represents_company""" %
		', '.join(['%s']*len(invoice_list)), tuple([inv.name for inv in invoice_list]), as_dict=1)

	internal_invoice_map = {}
	for d in unrealized_amount_details:
		if d.unrealized_profit_loss_account:
			internal_invoice_map.setdefault((d.name, d.unrealized_profit_loss_account), d.amount)

	return internal_invoice_map

def get_invoice_tax_map(invoice_list, invoice_income_map, income_accounts):
	tax_details = frappe.db.sql("""select parent, account_head,
	sum(base_tax_amount_after_discount_amount) as tax_amount
	from `tabSales Taxes and Charges` where parent in (%s) group by parent, account_head""" %
	', '.join(['%s']*len(invoice_list)), tuple([inv.name for inv in invoice_list]), as_dict=1)

	invoice_tax_map = {}
	for d in tax_details:
		if d.account_head in income_accounts:
			if d.account_head in invoice_income_map[d.parent]:
				invoice_income_map[d.parent][d.account_head] += flt(d.tax_amount)
			else:
				invoice_income_map[d.parent][d.account_head] = flt(d.tax_amount)
		else:
			invoice_tax_map.setdefault(d.parent, frappe._dict()).setdefault(d.account_head, [])
			invoice_tax_map[d.parent][d.account_head] = flt(d.tax_amount)

	return invoice_income_map, invoice_tax_map

def get_invoice_so_dn_map(invoice_list):
	si_items = frappe.db.sql("""select parent, sales_order, delivery_note, so_detail
		from `tabSales Invoice Item` where parent in (%s)
		and (ifnull(sales_order, '') != '' or ifnull(delivery_note, '') != '')""" %
		', '.join(['%s']*len(invoice_list)), tuple([inv.name for inv in invoice_list]), as_dict=1)

	invoice_so_dn_map = {}
	for d in si_items:
		if d.sales_order:
			invoice_so_dn_map.setdefault(d.parent, frappe._dict()).setdefault(
				"sales_order", []).append(d.sales_order)

		delivery_note_list = None
		if d.delivery_note:
			delivery_note_list = [d.delivery_note]
		elif d.sales_order:
			delivery_note_list = frappe.db.sql_list("""select distinct parent from `tabDelivery Note Item`
				where docstatus=1 and so_detail=%s""", d.so_detail)

		if delivery_note_list:
			invoice_so_dn_map.setdefault(d.parent, frappe._dict()).setdefault("delivery_note", delivery_note_list)

	return invoice_so_dn_map
def get_invoice_cc_wh_map(invoice_list):
	si_items = frappe.db.sql("""select parent, cost_center, warehouse
		from `tabSales Invoice Item` where parent in (%s)
		and (ifnull(cost_center, '') != '' or ifnull(warehouse, '') != '')""" %
		', '.join(['%s']*len(invoice_list)), tuple([inv.name for inv in invoice_list]), as_dict=1)

	invoice_cc_wh_map = {}
	for d in si_items:
		if d.cost_center:
			invoice_cc_wh_map.setdefault(d.parent, frappe._dict()).setdefault(
				"cost_center", []).append(d.cost_center)

		if d.warehouse:
			invoice_cc_wh_map.setdefault(d.parent, frappe._dict()).setdefault(
				"warehouse", []).append(d.warehouse)

	return invoice_cc_wh_map

def get_invoice_cc_wh_map_group(invoice_list):
	si_items = frappe.db.sql("""select distinct  cost_center
		from `tabSales Invoice Item` where parent in (%s)
		and (ifnull(cost_center, '') != '' or ifnull(warehouse, '') != '') 
		""" %
		', '.join(['%s']*len(invoice_list)), tuple([inv.name for inv in invoice_list]), as_dict=1)
	
	invoice_cc_wh_map_group = {}
	for d in si_items:
		if d.cost_center:
			invoice_cc_wh_map_group.setdefault(
				"cost_center", []).append(d.cost_center)

		

	
	return invoice_cc_wh_map_group

def get_mode_of_payments(invoice_list):
	mode_of_payments = {}
	if invoice_list:
		inv_mop = frappe.db.sql("""select parent, mode_of_payment
			from `tabSales Invoice Payment` where parent in (%s) group by parent, mode_of_payment""" %
			', '.join(['%s']*len(invoice_list)), tuple(invoice_list), as_dict=1)

		for d in inv_mop:
			mode_of_payments.setdefault(d.parent, []).append(d.mode_of_payment)

	return mode_of_payments
