# Que_3:-  Convert the tuple order = ('Burger', 'Fries', 'Coke') into a list, add 'Ice Cream' to the end, then convert it back to a tuple and print the final tuple.

order = ('Burger', 'Fries', 'Coke')

# Convert tuple to list
order_list = list(order)

# Add a new item
order_list.append('Ice Cream')

# Convert list back to tuple
order = tuple(order_list)

print(order)