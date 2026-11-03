"""Vending Machine Restocking Alert System."""

inventory = {
    "Water Bottle": {"quantity": 5, "threshold": 10},
    "Chips": {"quantity": 20, "threshold": 5},
    "Chocolate": {"quantity": 3, "threshold": 8},
    "Juice": {"quantity": 15, "threshold": 5}
}


def check_stock(product):
    if product not in inventory:
        return "Product Not Found"

    quantity = inventory[product]["quantity"]
    threshold = inventory[product]["threshold"]

    if quantity <= threshold:
        return "Low Stock"
    return "Stock Sufficient"


def generate_alerts():
    alerts = []

    for product, details in inventory.items():
        if details["quantity"] <= details["threshold"]:
            alerts.append(product)

    return alerts


def restock_product(product, amount):
    if product not in inventory:
        return "Product Not Found"

    if amount <= 0:
        return "Invalid Quantity"

    inventory[product]["quantity"] += amount

    return "Restocking Successful"