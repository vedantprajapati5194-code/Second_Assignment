# Que_1:- Create a dynamic nested dictionary in Python to represent a Flipkart shopping cart where each user (by username) can have multiple items, and each item has a name, quantity, and price. Add two users with at least two items each, then print the entire cart.

# Create an empty shopping cart
cart = {}

# Add first user
cart["Rahul"] = {
    "item1": {
        "name": "Shoes",
        "quantity": 2,
        "price": 1500
    },
    "item2": {
        "name": "Bag",
        "quantity": 1,
        "price": 1200
    }
}

# Add second user
cart["Priya"] = {
    "item1": {
        "name": "Headphones",
        "quantity": 1,
        "price": 2200
    },
    "item2": {
        "name": "Watch",
        "quantity": 2,
        "price": 1800
    }
}

# Print the entire cart
print(cart)