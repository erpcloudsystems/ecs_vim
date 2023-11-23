from __future__ import unicode_literals
import frappe
from frappe import _

frappe.whitelist()
def cron():
    # cleaning packed_items
    frappe.db.sql(f"""
                DELETE FROM `tabPacked Item`
                WHERE custom_pos_closing_entry IS NOT NULL
        """)