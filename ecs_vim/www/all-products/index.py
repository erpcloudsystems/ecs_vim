import frappe
from erpnext.e_commerce.product_data_engine.query import ProductQuery
from erpnext.e_commerce.product_data_engine.filters import ProductFiltersBuilder

sitemap = 1

def get_context(context):
	if frappe.form_dict:
		search = frappe.form_dict.search
		field_filters = frappe.parse_json(frappe.form_dict.field_filters)
		attribute_filters = frappe.parse_json(frappe.form_dict.attribute_filters)
		start = frappe.parse_json(frappe.form_dict.start)
	else:
		field_filters= {}
		search  = attribute_filters = None
		start = 0

	engine = ProductQuery()

	context.items = engine.query(attribute_filters, field_filters, search, start)["items"]
	# Add homepage as parent
	context.parents = [{"name": frappe._("Home"), "route":"/"}]
	product_settings = frappe.get_doc("E Commerce Settings")
	# product_settings = get_product_settings()
	filter_engine = ProductFiltersBuilder()

	context.field_filters = filter_engine.get_field_filters()
	context.attribute_filters = filter_engine.get_attribute_filters() 

	context.product_settings = product_settings
	context.body_class = "product-page"
	context.page_length = product_settings.products_per_page or 20

	context.no_cache = 1
	return context