# Que_4:-You have two lists: one with Zomato restaurant names ['Burger Hub', 'Pizza Point', 'Sushi House'] and another with their delivery times in minutes [30, 25, 40]. Use the zip() function to pair each restaurant with its delivery time and print each pair in the format: 'Burger Hub - 30 min'.


# bassically this used to combined to lists


restaurants = ['Burger Hub', 'Pizza Point', 'Sushi House']
delivery_times = [30, 25, 40]

for restaurant, time in zip(restaurants, delivery_times):
    print(restaurant, "-", time, "min")