# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


import json

import frappe
from frappe import _
from frappe.core.page.background_jobs.background_jobs import get_info
from frappe.model.document import Document
from frappe.model.mapper import map_child_doc, map_doc
from frappe.utils import cint, flt, get_time, getdate, nowdate, nowtime
from frappe.utils.background_jobs import enqueue
from frappe.utils.scheduler import is_scheduler_inactive
from erpnext.accounts.doctype.pos_invoice_merge_log.pos_invoice_merge_log import update_item_wise_tax_detail
from erpnext.stock.get_item_details import get_item_details, get_price_list_rate


def update_packing_list(self):
    if cint(self.update_stock) == 1:
        
        make_packing_list(self)
    else:
        self.set("packed_items", [])
def on_submit_si(doc, seleceted_packed_items):
    if seleceted_packed_items:
        selected_packed_items_refactor = []
        for item in seleceted_packed_items:
            found = False
            for i in selected_packed_items_refactor:
                if (
                    i["parent_item"] == item["parent_item"]
                    and i["item_code"] == item["item_code"]
                ):
                    found = True
                    i["packed_quantity"] = i["packed_quantity"] + item["packed_quantity"]
                    i["combo_qty"] = i["combo_qty"] + item["combo_qty"]
                    i["quantity"] = i["quantity"] + item["quantity"]
                    i["qty"] = i["qty"] + item["qty"] 


            if not found:
                selected_packed_items_refactor.append(item)
        doc.packed_items = []
        doc.set("packed_items", selected_packed_items_refactor)
@frappe.whitelist()
def process_merging_into_sales_invoice(self, data):
        sales_invoice = self.get_new_sales_invoice()

        sales_invoice, seleceted_packed_items = self.merge_pos_invoice_into(sales_invoice, data)

        sales_invoice.is_consolidated = 1
        sales_invoice.set_posting_time = 1
        sales_invoice.posting_date = getdate(self.posting_date)
        sales_invoice.posting_time = get_time(self.posting_time)
        sales_invoice.save()
        if seleceted_packed_items:
            on_submit_si(sales_invoice, seleceted_packed_items)
        sales_invoice.submit()

        self.consolidated_invoice = sales_invoice.name
        
        return sales_invoice.name

def process_merging_into_credit_note(self, data):
    credit_note = self.get_new_sales_invoice()
    credit_note.is_return = 1

    credit_note, seleceted_packed_items = self.merge_pos_invoice_into(credit_note, data)

    credit_note.is_consolidated = 1
    credit_note.set_posting_time = 1
    credit_note.posting_date = getdate(self.posting_date)
    credit_note.posting_time = get_time(self.posting_time)
    # TODO: return could be against multiple sales invoice which could also have been consolidated?
    # credit_note.return_against = self.consolidated_invoice
    credit_note.save()
    if seleceted_packed_items:
        on_submit_si(credit_note, seleceted_packed_items)
    credit_note.submit()

    self.consolidated_credit_note = credit_note.name

    return credit_note.name
@frappe.whitelist()
def merge_pos_invoice_into(self, invoice, data):
        items, payments, taxes = [], [], []
        seleceted_packed_items = []
        loyalty_amount_sum, loyalty_points_sum = 0, 0
        rounding_adjustment, base_rounding_adjustment = 0, 0
        rounded_total, base_rounded_total = 0, 0
        loyalty_amount_sum, loyalty_points_sum, idx = 0, 0, 1
        for doc in data:
            if doc.get("seleceted_packed_items"):
                for item in doc.get("seleceted_packed_items"):
                    seleceted_packed_items.append({
                        "parent_item":item.parent_item,
                        "item_code":item.item_code,
                        "packed_quantity":item.packed_quantity,
                        "set_no":item.set_no,
                        "combo_qty":item.combo_qty,
                        "quantity":item.quantity,
                        "default_item":item.default_item,
                        "parent_detail_docname":item.parent_detail_docname,
                        "qty":item.quantity,
                        "custom_pos_closing_entry":self.pos_closing_entry,
                        "consolidated_invoice":self.consolidated_invoice,
                    })
            map_doc(doc, invoice, table_map={"doctype": invoice.doctype})

            if doc.redeem_loyalty_points:
                invoice.loyalty_redemption_account = doc.loyalty_redemption_account
                invoice.loyalty_redemption_cost_center = doc.loyalty_redemption_cost_center
                loyalty_points_sum += doc.loyalty_points
                loyalty_amount_sum += doc.loyalty_amount

            for item in doc.get("items"):
                found = False
                for i in items:
                    if (
                        i.item_code == item.item_code
                        and not i.serial_no
                        and not i.batch_no
                        and i.uom == item.uom
                        and i.net_rate == item.net_rate
                        and i.warehouse == item.warehouse
                    ):
                        found = True
                        i.qty = i.qty + item.qty
                        i.amount = i.amount + item.net_amount
                        i.net_amount = i.amount
                        i.base_amount = i.base_amount + item.base_net_amount
                        i.base_net_amount = i.base_amount


                if not found:
                    item.rate = item.net_rate
                    item.amount = item.net_amount
                    item.base_amount = item.base_net_amount
                    item.price_list_rate = 0
                    si_item = map_child_doc(item, invoice, {"doctype": "Sales Invoice Item"})
                    items.append(si_item)

            for tax in doc.get("taxes"):
                found = False
                for t in taxes:
                    if t.account_head == tax.account_head and t.cost_center == tax.cost_center:
                        t.tax_amount = flt(t.tax_amount) + flt(tax.tax_amount_after_discount_amount)
                        t.base_tax_amount = flt(t.base_tax_amount) + flt(tax.base_tax_amount_after_discount_amount)
                        update_item_wise_tax_detail(t, tax)
                        found = True
                if not found:
                    tax.charge_type = "Actual"
                    tax.idx = idx
                    idx += 1
                    tax.included_in_print_rate = 0
                    tax.tax_amount = tax.tax_amount_after_discount_amount
                    tax.base_tax_amount = tax.base_tax_amount_after_discount_amount
                    tax.item_wise_tax_detail = tax.item_wise_tax_detail
                    taxes.append(tax)

            for payment in doc.get("payments"):
                found = False
                for pay in payments:
                    if pay.account == payment.account and pay.mode_of_payment == payment.mode_of_payment:
                        pay.amount = flt(pay.amount) + flt(payment.amount)
                        pay.base_amount = flt(pay.base_amount) + flt(payment.base_amount)
                        found = True
                if not found:
                    payments.append(payment)

            rounding_adjustment += doc.rounding_adjustment
            rounded_total += doc.rounded_total
            base_rounding_adjustment += doc.base_rounding_adjustment
            base_rounded_total += doc.base_rounded_total

        if loyalty_points_sum:
            invoice.redeem_loyalty_points = 1
            invoice.loyalty_points = loyalty_points_sum
            invoice.loyalty_amount = loyalty_amount_sum

        invoice.set("items", items)
        invoice.set("payments", payments)
        invoice.set("taxes", taxes)
        invoice.set("rounding_adjustment", rounding_adjustment)
        invoice.set("base_rounding_adjustment", base_rounding_adjustment)
        invoice.set("rounded_total", rounded_total)
        invoice.set("base_rounded_total", base_rounded_total)
        invoice.additional_discount_percentage = 0
        invoice.discount_amount = 0.0
        invoice.taxes_and_charges = None
        invoice.ignore_pricing_rule = 1
        invoice.customer = self.customer
        invoice.disable_rounded_total = cint(
            frappe.db.get_value("POS Profile", invoice.pos_profile, "disable_rounded_total")
        )

        if self.merge_invoices_based_on == "Customer Group":
            invoice.flags.ignore_pos_profile = True
            invoice.pos_profile = ""

        return invoice, seleceted_packed_items


# erpnext packed_item 

def make_packing_list(doc):
    "Make/Update packing list for Product Bundle Item."
    if doc.get("_action") and doc._action == "update_after_submit":
        return

    parent_items_price, reset = {}, False
    set_price_from_children = frappe.db.get_single_value(
        "Selling Settings", "editable_bundle_item_rates"
    )

    stale_packed_items_table = get_indexed_packed_items_table(doc)

    reset = reset_packing_list(doc)

    for item_row in doc.get("items"):
        if is_product_bundle(item_row.item_code):
            
            for bundle_item in get_product_bundle_items(item_row.item_code,item_row.qty, doc):
                pi_row = add_packed_item_row(
                    doc=doc,
                    packing_item=bundle_item,
                    main_item_row=item_row,
                    packed_items_table=stale_packed_items_table,
                    reset=reset,
                )
                item_data = get_packed_item_details(bundle_item.item_code, doc.company)
                update_packed_item_basic_data(item_row, pi_row, bundle_item, item_data)
                update_packed_item_stock_data(item_row, pi_row, bundle_item, item_data, doc)
                update_packed_item_price_data(pi_row, item_data, doc)
                update_packed_item_from_cancelled_doc(item_row, bundle_item, pi_row, doc)

                if set_price_from_children:  # create/update bundle item wise price dict
                    update_product_bundle_rate(parent_items_price, pi_row, item_row)

    if parent_items_price:
        set_product_bundle_rate_amount(doc, parent_items_price)  # set price in bundle item


def is_product_bundle(item_code: str) -> bool:
    return bool(frappe.db.exists("Product Bundle", {"new_item_code": item_code}))


def get_indexed_packed_items_table(doc):
    """
    Create dict from stale packed items table like:
    {(Parent Item 1, Bundle Item 1, ae4b5678): {...}, (key): {value}}

    Use: to quickly retrieve/check if row existed in table instead of looping n times
    """
    indexed_table = {}
    for packed_item in doc.get("packed_items"):
        key = (packed_item.parent_item, packed_item.item_code, packed_item.parent_detail_docname)
        indexed_table[key] = packed_item

    return indexed_table


def reset_packing_list(doc):
    "Conditionally reset the table and return if it was reset or not."
    reset_table = False
    doc_before_save = doc.get_doc_before_save()

    if doc_before_save:
        # reset table if:
        # 1. items were deleted
        # 2. if bundle item replaced by another item (same no. of items but different items)
        # we maintain list to track recurring item rows as well
        items_before_save = [(item.name, item.item_code) for item in doc_before_save.get("items")]
        items_after_save = [(item.name, item.item_code) for item in doc.get("items")]
        reset_table = items_before_save != items_after_save
    else:
        # reset: if via Update Items OR
        # if new mapped doc with packed items set (SO -> DN)
        # (cannot determine action)
        reset_table = True

    if reset_table:
        doc.set("packed_items", [])
    return reset_table


def get_product_bundle_items(item_code,item_qty, self):
    class PackedItems():
        def __init__(self, item_code, qty, stock_uom, description):
            self.item_code = item_code
            self.qty = qty / item_qty 
            self.stock_uom = stock_uom or None
            self.descriptions = description or None
    packed_items = []
    for row in self.packed_items: # 39
        if row.parent_item == item_code:
            packed_items.append(PackedItems(**{
                "item_code":row.item_code,
                "qty":row.qty,
                "stock_uom": frappe.db.get_value("Item", row.item_code, ["stock_uom"]),
                "description":frappe.db.get_value("Item", row.item_code, ["description"]),
            }))
            self.packed_items.remove(row)

    return packed_items
    


def add_packed_item_row(doc, packing_item, main_item_row, packed_items_table, reset):
    """Add and return packed item row.
    doc: Transaction document
    packing_item (dict): Packed Item details
    main_item_row (dict): Items table row corresponding to packed item
    packed_items_table (dict): Packed Items table before save (indexed)
    reset (bool): State if table is reset or preserved as is
    """
    exists, pi_row = False, {}

    # check if row already exists in packed items table
    key = (main_item_row.item_code, packing_item.item_code, main_item_row.name)
    if packed_items_table.get(key):
        pi_row, exists = packed_items_table.get(key), True

    if not exists:
        pi_row = doc.append("packed_items", {})
    elif reset:  # add row if row exists but table is reset
        pi_row.idx, pi_row.name = None, None
        pi_row = doc.append("packed_items", pi_row)

    return pi_row


def get_packed_item_details(item_code, company):
    item = frappe.qb.DocType("Item")
    item_default = frappe.qb.DocType("Item Default")
    query = (
        frappe.qb.from_(item)
        .left_join(item_default)
        .on((item_default.parent == item.name) & (item_default.company == company))
        .select(
            item.item_name,
            item.is_stock_item,
            item.description,
            item.stock_uom,
            item.valuation_rate,
            item_default.default_warehouse,
        )
        .where(item.name == item_code)
    )
    return query.run(as_dict=True)[0]


def update_packed_item_basic_data(main_item_row, pi_row, packing_item, item_data):
    pi_row.parent_item = main_item_row.item_code
    pi_row.parent_detail_docname = main_item_row.name
    pi_row.item_code = packing_item.item_code
    pi_row.item_name = item_data.item_name
    pi_row.uom = item_data.stock_uom
    pi_row.qty = flt(packing_item.qty) * flt(main_item_row.stock_qty)
    pi_row.conversion_factor = main_item_row.conversion_factor

    if not pi_row.description:
        pi_row.description = packing_item.descriptions


def update_packed_item_stock_data(main_item_row, pi_row, packing_item, item_data, doc):
    # TODO batch_no, actual_batch_qty, incoming_rate
    if not pi_row.warehouse and not doc.amended_from:
        fetch_warehouse = doc.get("is_pos") or item_data.is_stock_item or not item_data.default_warehouse
        pi_row.warehouse = (
            main_item_row.warehouse
            if (fetch_warehouse and main_item_row.warehouse)
            else item_data.default_warehouse
        )

    if not pi_row.target_warehouse:
        pi_row.target_warehouse = main_item_row.get("target_warehouse")

    bin = get_packed_item_bin_qty(packing_item.item_code, pi_row.warehouse)
    pi_row.actual_qty = flt(bin.get("actual_qty"))
    pi_row.projected_qty = flt(bin.get("projected_qty"))


def update_packed_item_price_data(pi_row, item_data, doc):
    "Set price as per price list or from the Item master."
    if pi_row.rate:
        return

    item_doc = frappe.get_cached_doc("Item", pi_row.item_code)
    row_data = pi_row.as_dict().copy()
    row_data.update(
        {
            "company": doc.get("company"),
            "price_list": doc.get("selling_price_list"),
            "currency": doc.get("currency"),
            "conversion_rate": doc.get("conversion_rate"),
        }
    )
    if not row_data.get("transaction_date"):
        row_data.update({"transaction_date": doc.get("transaction_date")})

    rate = get_price_list_rate(row_data, item_doc).get("price_list_rate")

    pi_row.rate = rate or item_data.get("valuation_rate") or 0.0


def update_packed_item_from_cancelled_doc(main_item_row, packing_item, pi_row, doc):
    "Update packed item row details from cancelled doc into amended doc."
    prev_doc_packed_items_map = None
    if doc.amended_from:
        prev_doc_packed_items_map = get_cancelled_doc_packed_item_details(doc.packed_items)

    if prev_doc_packed_items_map and prev_doc_packed_items_map.get(
        (packing_item.item_code, main_item_row.item_code)
    ):
        prev_doc_row = prev_doc_packed_items_map.get((packing_item.item_code, main_item_row.item_code))
        pi_row.batch_no = prev_doc_row[0].batch_no
        pi_row.serial_no = prev_doc_row[0].serial_no
        pi_row.warehouse = prev_doc_row[0].warehouse


def get_packed_item_bin_qty(item, warehouse):
    bin_data = frappe.db.get_values(
        "Bin",
        fieldname=["actual_qty", "projected_qty"],
        filters={"item_code": item, "warehouse": warehouse},
        as_dict=True,
    )

    return bin_data[0] if bin_data else {}


def get_cancelled_doc_packed_item_details(old_packed_items):
    prev_doc_packed_items_map = {}
    for items in old_packed_items:
        prev_doc_packed_items_map.setdefault((items.item_code, items.parent_item), []).append(
            items.as_dict()
        )
    return prev_doc_packed_items_map


def update_product_bundle_rate(parent_items_price, pi_row, item_row):
    """
    Update the price dict of Product Bundles based on the rates of the Items in the bundle.

    Stucture:
    {(Bundle Item 1, ae56fgji): 150.0, (Bundle Item 2, bc78fkjo): 200.0}
    """
    key = (pi_row.parent_item, pi_row.parent_detail_docname)
    rate = parent_items_price.get(key)
    if not rate:
        parent_items_price[key] = 0.0

    parent_items_price[key] += flt((pi_row.rate * pi_row.qty) / item_row.stock_qty)


def set_product_bundle_rate_amount(doc, parent_items_price):
    "Set cumulative rate and amount in bundle item."
    for item in doc.get("items"):
        bundle_rate = parent_items_price.get((item.item_code, item.name))
        if bundle_rate and bundle_rate != item.rate:
            item.rate = bundle_rate
            item.amount = flt(bundle_rate * item.qty)


def on_doctype_update():
    frappe.db.add_index("Packed Item", ["item_code", "warehouse"])


@frappe.whitelist()
def get_items_from_product_bundle(row):
    row, items = json.loads(row), []

    bundled_items = get_product_bundle_items(row["item_code"])
    for item in bundled_items:
        row.update({"item_code": item.item_code, "qty": flt(row["quantity"]) * flt(item.qty)})
        items.append(get_item_details(row))

    return items
