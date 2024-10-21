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
            "label": _("Item Code"),
            "fieldname": "item_code",
            "fieldtype": "Link",
            "options": "Item",
            "width": 120,
        },
        {"label": _("Item Name"), "fieldname": "item_name", "fieldtype": "Data", "width": 120},
        {"label": _("Brand"), "fieldname": "brand", "fieldtype": "Data", "width": 100},
        {
            "label": _("Warehouse"),
            "fieldname": "warehouse",
            "fieldtype": "Link",
            "options": "Warehouse",
            "width": 120,
        },
        {
            "label": _("Stock Available"),
            "fieldname": "stock_available",
            "fieldtype": "Float",
            "width": 120,
        },
        {
            "label": _("Selling Price List"),
            "fieldname": "selling_price_list",
            "fieldtype": "Link",
            "options": "Price List",
            "width": 120,
        },
        {"label": _("Selling Rate"), "fieldname": "selling_rate", "fieldtype": "Currency", "width": 120},
    ]


def get_data(filters):
    item_price_qty_data = get_item_price_qty_data(filters)
    return item_price_qty_data


def get_item_price_qty_data(filters):
    item_price = frappe.qb.DocType("Item Price")
    bin = frappe.qb.DocType("Bin")

    query = (
        frappe.qb.from_(item_price)
        .left_join(bin)
        .on(item_price.item_code == bin.item_code)
        .select(
            item_price.item_code,
            item_price.item_name,
            item_price.brand.as_("brand"),
            bin.warehouse.as_("warehouse"),
            bin.actual_qty.as_("actual_qty"),
            item_price.price_list.as_("price_list"),
            item_price.price_list_rate.as_("selling_rate")
        )
        .where(item_price.price_list == "Main Store Price")
        .where(item_price.selling == 1)
    )

    if filters.get("item_code"):
        query = query.where(item_price.item_code == filters.get("item_code"))

    item_results = query.run(as_dict=True)
    return item_results


@frappe.whitelist()
def get_items_with_main_store_price():
    # Get distinct items with "Main Store Price" set for selling
    item_price_list = frappe.db.get_list(
        "Item Price",
        filters={"price_list": "Main Store Price", "selling": 1},
        fields=["item_code"],
        distinct=True
    )

    # Extract item codes from the result
    item_codes = [item["item_code"] for item in item_price_list]
    
    # Return filtered items for the item_code filter in the JS report
    return {"filters": [["Item", "name", "in", item_codes]]}
