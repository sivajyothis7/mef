// Copyright (c) 2024, siva and contributors
// For license information, please see license.txt

frappe.query_reports["Item Stock Report"] = {
	filters: [
		{
			fieldname: "item_code",
			label: __("Item"),
			fieldtype: "Link",
			options: "Item",
		},
	],
};