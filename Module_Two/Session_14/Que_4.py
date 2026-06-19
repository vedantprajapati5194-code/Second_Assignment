# Que_4:- Given a nested dictionary representing Zomato orders (order_id as key, value is another dictionary with 'restaurant', 'items' (list), and 'total'), write a function to add a new order and another function to update the total of an existing order.<br><br><em><strong>Hint:</strong> Use dict.setdefault() to handle missing keys dynamically.</em>

# Dictionary to store orders
orders = {}


# Function to add a new order
def add_order(orders, order_id, restaurant, items, total):
    orders.setdefault(order_id, {
        "restaurant": restaurant,
        "items": items,
        "total": total
    })


# Function to update an existing order's total
def update_total(orders, order_id, new_total):
    if order_id in orders:
        orders[order_id]["total"] = new_total
    else:
        print("Order not found!")


# Add orders
add_order(
    orders,
    101,
    "Pizza Hut",
    ["Pizza", "Garlic Bread"],
    550
)

add_order(
    orders,
    102,
    "Burger King",
    ["Burger", "Fries"],
    300
)

# Update total of order 101
update_total(orders, 101, 600)

# Print all orders
print(orders)