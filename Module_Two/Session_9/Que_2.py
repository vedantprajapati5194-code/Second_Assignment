# Que_2:- Given a list of food item prices from a Zomato order: [120, 250, 99, 180, 310], use a lambda function with the map() function to add a 10% service charge to each price and print the updated list.


# List of food item prices
prices = [120, 250, 99, 180, 310]

# Add 10% service charge to each price
updated_prices = list(map(lambda price: price * 1.10, prices))

# Print updated prices
print(updated_prices)
