// Copyright (c) 2024, siva and contributors
// For license information, please see license.txt

frappe.query_reports["Item Stock"] = {
    filters: [
        {
            fieldname: "item_code",
            label: __("Item Code"),
            fieldtype: "Link",
            options: "Item",
            default: null, // Optional: If you want to have a default value
            reqd: 0, // Optional: Set to 1 if this filter is required
        },
        // {
        //     fieldname: "warehouse",
        //     label: __("Warehouse"),
        //     fieldtype: "Link",
        //     options: "Warehouse",
        //     default: "Main Store", // Default to Main Store if required
        //     reqd: 1 // This ensures the Main Store is always selected
        // },
        {
            fieldname: "selling_price_list",
            label: __("Selling Price List"),
            fieldtype: "Link",
            options: "Price List",
            default: "Main Store Price", // Ensure only Main Store Price is used
            reqd: 1 // Set required to enforce filtering based on Main Store Price
        }
    ]
};
