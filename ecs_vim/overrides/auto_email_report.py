# Copyright (c) 2015, Frappe Technologies and contributors
# License: MIT. See LICENSE

import calendar
from datetime import timedelta

import frappe
from frappe import _
from frappe.desk.query_report import build_xlsx_data
from frappe.model.document import Document
from frappe.model.naming import append_number_if_name_exists
from frappe.utils import (
	add_to_date,
	cint,
	format_time,
	get_link_to_form,
	get_url_to_report,
	global_date_format,
	now,
	now_datetime,
	today,
	validate_email_address,
)
from frappe.utils.csvutils import to_csv
from frappe.utils.xlsxutils import make_xlsx
from frappe.email.doctype.auto_email_report import AutoEmailReport

class AutoEmailReportOverrides(AutoEmailReport):
	def get_report_content(self):
		"""Returns file in for the report in given format"""
		report = frappe.get_doc("Report", self.report)

		self.filters = frappe.parse_json(self.filters) if self.filters else {}

		if self.report_type == "Report Builder" and self.data_modified_till:
			self.filters["modified"] = (">", now_datetime() - timedelta(hours=self.data_modified_till))

		if self.report_type != "Report Builder" and self.dynamic_date_filters_set():
			self.prepare_dynamic_filters()

		columns, data = report.get_data(
			limit=self.no_of_rows or 100,
			user=self.user,
			filters=self.filters,
			as_dict=True,
			ignore_prepared_report=True,
			are_default_filters=False,
		)

		monthlycolumns, monthly_data = report.get_data(
			limit=self.no_of_rows or 100,
			user=self.user,
			filters={

			},
			as_dict=True,
			ignore_prepared_report=True,
			are_default_filters=False,
		)
		# add serial numbers
		columns.insert(0, frappe._dict(fieldname="idx", label="", width="30px"))
		for i in range(len(data)):
			data[i]["idx"] = i + 1

		if len(data) == 0 and self.send_if_data:
			return None

		if self.format == "HTML":
			columns, data = make_links(columns, data)
			columns = update_field_types(columns)
			return self.get_html_table(columns, data)

		elif self.format == "XLSX":
			report_data = frappe._dict()
			report_data["columns"] = columns
			report_data["result"] = data

			xlsx_data, column_widths = build_xlsx_data(report_data, [], 1, ignore_visible_idx=True)
			xlsx_file = make_xlsx(xlsx_data, "Auto Email Report", column_widths=column_widths)
			return xlsx_file.getvalue()

		elif self.format == "CSV":
			report_data = frappe._dict()
			report_data["columns"] = columns
			report_data["result"] = data

			xlsx_data, column_widths = build_xlsx_data(report_data, [], 1, ignore_visible_idx=True)
			return to_csv(xlsx_data)

		else:
			frappe.throw(_("Invalid Output Format"))
	def send(self):
		if self.filter_meta and not self.filters:
			frappe.throw(_("Please set filters value in Report Filter table."))

		data = self.get_report_content()
		if not data:
			return

		attachments = None
		if self.format == "HTML":
			message = data
		else:
			message = self.get_html_table()

		if not self.format == "HTML":
			attachments = [{"fname": self.get_file_name(), "fcontent": data}]

		frappe.sendmail(
			recipients=self.email_to.split(),
			subject=self.name,
			message=message,
			attachments=attachments,
			reference_doctype=self.doctype,
			reference_name=self.name,
		)