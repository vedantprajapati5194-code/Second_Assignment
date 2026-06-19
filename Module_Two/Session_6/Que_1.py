# Que_1:-Given two lists — one of product names and one of their prices — use the zip() function to create a dictionary mapping each product to its price, then print the dictionary.

# List of product names
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

# List of prices
prices = [50000, 500, 1500, 12000]

# Create dictionary using zip()
product_price = dict(zip(products, prices))

# Print the dictionary
print(product_price)
