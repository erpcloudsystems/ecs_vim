# -*- coding: utf-8 -*-
# Copyright (c) 2021, Tushar Kuwar and contributors
# For license information, please see license.txt
import frappe
import pyqrcode
import io, sys, base64

@frappe.whitelist()
def get_qr(data):
    getbase_data = get_base_qr(data)
    c = pyqrcode.create(getbase_data, error="M")
    s = io.BytesIO()
    c.png(s, scale=2)
    encoded = base64.b64encode(s.getvalue()).decode("ascii")
    return '<img src="data:image/png;base64,' + encoded + '">'


def get_base_qr(list_data):
    data_dict = list_data
    result = ""
    for data in data_dict:
        _tag = data[0]
        _val = data[1]

        tag_hex = hex(int(_tag))[2:].zfill(2)
        if sys.version_info.major == 3:
            vlen_hex = hex(len(_val.encode("utf8")))[2:].zfill(2)
            val_hex = _val.encode("utf8").hex()
        else:
            vlen_hex = hex(len(_val))[2:].zfill(2)
            val_hex = _val.encode("hex")
        result = result + (tag_hex + vlen_hex + val_hex)

    if sys.version_info.major == 3:
        result = base64.b64encode(bytes.fromhex(result))
    else:
        result = base64.b64encode(result.decode("hex"))

    return result.decode("ascii")
