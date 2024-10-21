// Copyright (c) 2024, siva and contributors
// For license information, please see license.txt

frappe.query_reports["Item Stock"] = {
    filters: [
        {
            fieldname: "item_code",
            label: __("Item"),
            fieldtype: "Link",
            options: "Item",
            get_query: function () {
                return {
                    query: "mef_custom.report.item_stock.item_stock.get_items_with_main_store_price"
                };
            }
        }
    ]
};
