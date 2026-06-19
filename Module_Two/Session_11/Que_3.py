# Que_3:- Create a Zomato order bill calculator that uses math.floor() to show the final bill amount after applying a 10% discount, rounding down to the nearest rupee.

import math

# Original bill amount
bill_amount = 850

# Calculate 10% discount
discount = bill_amount * 0.10

# Final amount after discount
final_bill = bill_amount - discount

# Round down to the nearest rupee
final_bill = math.floor(final_bill)

print("Original Bill:", bill_amount)
print("Discount (10%):", discount)
print("Final Bill:", final_bill)