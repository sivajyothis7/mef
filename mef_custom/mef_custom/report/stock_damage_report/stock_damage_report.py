# Copyright (c) 2024, siva and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    columns, data = [], []
    
    columns = get_columns()
    data = get_data(filters)
    
    return columns, data

def get_columns():
    return [
        {
            "label": _("Item Name"),
            "fieldname": "item_name",
            "fieldtype": "Link",
            "options": "Item",
            "width": 150
        },
        {
            "label": _("Status"),
            "fieldname": "status",
            "fieldtype": "Select",
            "options": "Damage Solved\nPending",
            "width": 120
        },
        {
            "label": _("Damage Description"),
            "fieldname": "damage_description",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("Current Warehouse"),
            "fieldname": "current_warehouse",
            "fieldtype": "Link",
            "options": "Warehouse",
            "width": 160
        }
    ]

def get_data(filters):
    query = """
        SELECT 
            item_name,
            status,
            damage_description,
            current_warehouse
        FROM 
            `tabStock Damage`
        WHERE
            1=1
    """
    
    if filters.get('status'):
        query += " AND status = %(status)s"
    if filters.get('item_name'):
        query += " AND item_name = %(item_name)s"
    if filters.get('current_warehouse'):
        query += " AND current_warehouse = %(current_warehouse)s"
    
    return frappe.db.sql(query, filters, as_dict=True)
