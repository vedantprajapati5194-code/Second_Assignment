# Que_2:- Build a Flipkart-style price rounder: given a list of product prices with decimals, use math.ceil() to round each price up to the nearest whole number and display the results.<br><br><em><strong>Hint:</strong> Try with prices like 199.1, 349.8, and 599.3.</em>

import math

# List of product prices
prices = [199.1, 349.8, 599.3]

print("Rounded Product Prices:")

for price in prices:
    rounded_price = math.ceil(price)
    print("Original Price:", price, "-> Rounded Price:", rounded_price)