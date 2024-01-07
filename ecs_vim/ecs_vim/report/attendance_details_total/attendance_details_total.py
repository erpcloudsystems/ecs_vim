# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from datetime import datetime


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters, columns)
    return columns, data


def get_columns():
    return [
        {
            "label": _("Code"),
            "fieldname": "code",
            "fieldtype": "Link",
            "options": "Employee",
            "width": 70
        },
        {
            "label": _("Name"),
            "fieldname": "employee_name",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("Apsent"),
            "fieldname": "num_absent",
            "fieldtype": "Int",
            "width": 200
        },
        {
            "label": _("present"),
            "fieldname": "num_present",
            "fieldtype": "Int",
            "width": 200
        },
        {
            "label": _("On Leave"),
            "fieldname": "On_Leave",
            "fieldtype": "Int",
            "width": 200
        },
        {
            "label": _("Half Day"),
            "fieldname": "Half_Day",
            "fieldtype": "Int",
            "width": 200
        },
        {
            "label": _("Total Lates"),
            "fieldname": "total_lates",
            "fieldtype": "Float",
            "width": 100
        },
        {
            "label": _("Total Early Come"),
            "fieldname": "total_early_come",
            "fieldtype": "Float",
            "width": 100
        }
        ,
        {
            "label": _("Early Overtime (min)"),
            "fieldname": "total_overtime",
            "fieldtype": "Float",
            "width": 100
        }
        ,
        {
            "label": _(" Early Leave (min)"),
            "fieldname": "total_early_leave",
            "fieldtype": "Float",
            "width": 100
        }
    ]


def get_data(filters, columns):
    item_price_qty_data = []
    item_price_qty_data = get_attendance_data(filters)
    return item_price_qty_data


def get_attendance_data(filters):
    from_dates = filters.get("from_date")
    to_dates = filters.get("to_date")
    conditions = ""
    # if 'department' in filters:
    # 	conditions.append(
    # 		f"(department = '{filters['department']}' )")
    # if 'employee' in filters:
    # 	conditions.append(
    # 		f"(employee = '{filters['employee']}' )")
    # if 'shift' in filters:
    # 	conditions.append(
    # 		f"(shift = '{filters['shift']}' )")
    if filters.get("department"):
        conditions += f" AND department = '{filters.get('department')}'"
    if filters.get("employee"):
        conditions += f" AND employee = '{filters.get('employee')}'"
    if filters.get("shift"):
        conditions += f" AND shift = '{filters.get('shift')}'"

    query = """
		SELECT
			employee as code,
			employee_name as employee_name,
			SUM(CASE
					WHEN (TIME_TO_SEC(TIME(in_time)) - TIME_TO_SEC((SELECT start_time FROM `tabShift Type` WHERE name = `tabAttendance`.shift ORDER BY creation DESC LIMIT 1))) < 0 THEN 0
					ELSE (TIME_TO_SEC(TIME(in_time)) - TIME_TO_SEC((SELECT start_time FROM `tabShift Type` WHERE name = `tabAttendance`.shift ORDER BY creation DESC LIMIT 1))) / 60
				END) AS total_lates,

			SUM(CASE
					WHEN (TIME_TO_SEC(TIME(in_time)) - TIME_TO_SEC((SELECT start_time FROM `tabShift Type` WHERE name = `tabAttendance`.shift ORDER BY creation DESC LIMIT 1))) > 0 THEN 0
					ELSE ABS((TIME_TO_SEC(TIME(in_time)) - TIME_TO_SEC((SELECT start_time FROM `tabShift Type` WHERE name = `tabAttendance`.shift ORDER BY creation DESC LIMIT 1))) / 60)
				END) AS total_early_come,

			SUM(CASE
					WHEN (TIME_TO_SEC(TIME(out_time)) - TIME_TO_SEC((SELECT end_time FROM `tabShift Type` WHERE name = `tabAttendance`.shift ORDER BY creation DESC LIMIT 1))) < 0 THEN 0
					ELSE (TIME_TO_SEC(TIME(out_time)) - TIME_TO_SEC((SELECT end_time FROM `tabShift Type` WHERE name = `tabAttendance`.shift ORDER BY creation DESC LIMIT 1))) / 60
				END) AS total_overtime,

			SUM(CASE
					WHEN (TIME_TO_SEC(TIME(out_time)) - TIME_TO_SEC((SELECT end_time FROM `tabShift Type` WHERE name = `tabAttendance`.shift ORDER BY creation DESC LIMIT 1))) > 0 THEN 0
					ELSE ABS((TIME_TO_SEC(TIME(out_time)) - TIME_TO_SEC((SELECT end_time FROM `tabShift Type` WHERE name = `tabAttendance`.shift ORDER BY creation DESC LIMIT 1))) / 60)
				END) AS total_early_leave,
			COUNT(CASE WHEN status = 'Absent' THEN 1 ELSE NULL END) AS num_absent,
    		COUNT(CASE WHEN status = 'Present' THEN 1 ELSE NULL END) AS num_present,
			COUNT(CASE WHEN status = 'On Leave' THEN 1 ELSE NULL END) AS On_Leave,
			COUNT(CASE WHEN status = 'Half Day' THEN 1 ELSE NULL END) AS Half_Day
		FROM
			`tabAttendance`
		WHERE
			docstatus = 1
			AND attendance_date BETWEEN '{from_dates}' AND '{to_dates}'
			{conditions}
		GROUP BY
			employee

	""".format(conditions=conditions, from_dates=from_dates, to_dates=to_dates)

    item_results = frappe.db.sql(query, as_dict=1)
    return item_results
    # frappe.msgprint(str(item_results))
    # result = []
    # if item_results:
    #     for item_dict in item_results:
    #         data = {
    #             'name': item_dict.name,
    #             'code': item_dict.code,
    #             'employee_name': item_dict.employee_name,
    #             'department': item_dict.department,
    #             'shift': item_dict.shift,
    #             'status': item_dict.status,
    #             'in_time': item_dict.in_time,
    #             'out_time': item_dict.out_time,
    #             'working_hours': item_dict.working_hours,
    #             'attendance_date': item_dict.attendance_date,
    #             'attendance_request': item_dict.attendance_request,
    #             'leave_application': item_dict.leave_application,
    #         }
    #         pp = frappe.get_last_doc('Shift Type', filters={"name": item_dict.shift})

    #         def calculate_difference(time1, time2):
    #             if time1 and time2:
    #                 time1 = datetime.strptime(str(time1.time()), '%H:%M:%S')
    #                 time2 = datetime.strptime(str(time2), '%H:%M:%S')
    #                 time_difference = (time1 - time2).total_seconds()
    #                 return int(time_difference) if time_difference > 0 else 0
    #             return 0

    #         data['lates'] = calculate_difference(item_dict.in_time, pp.start_time)
    #         data['overtime'] = calculate_difference(item_dict.out_time, pp.end_time)

    #         result.append(data)

    return result

