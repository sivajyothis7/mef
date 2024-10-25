// Copyright (c) 2024, siva and contributors
// For license information, please see license.txt

frappe.query_reports["Stock Damage Report"] = {
    "filters": [
        {
            "fieldname": "item_name",
            "label": __("Item Name"),
            "fieldtype": "Link",
            "options": "Item",
            "default": "",
            "width": 150
        },
        {
            "fieldname": "status",
            "label": __("Status"),
            "fieldtype": "Select",
            "options": "\nDamage Solved\nPending",
            "default": "",
            "width": 120
        },
        {
            "fieldname": "current_warehouse",
            "label": __("Current Warehouse"),
            "fieldtype": "Link",
            "options": "Warehouse",
            "default": "",
            "width": 160
        }
    ]
};
