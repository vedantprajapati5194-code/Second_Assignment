# Que_3:- Simulate a Flipkart shopping cart: prices = [299, 499, 150, 1200, 350]. Use a for loop to calculate and print the total cart value.

prices = [299, 499, 150, 1200, 350]

total = 0

for price in prices:
    total = total + price

print("Total cart value =", total)