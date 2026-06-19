# Que_3:- Simulate a Zomato-style restaurant menu using a nested dictionary: each restaurant name as a key, and its value as another dictionary with keys 'cuisine' and 'rating'. Add two restaurants, then update the rating of one restaurant to a new value.<br><br><em><strong>Hint:</strong> Use dictionary indexing to access and update the nested 'rating' value.</em>

restaurants = {
    "Pizza Point": {
        "cuisine": "Italian",
        "rating": 4.2
    },
    "Burger Hub": {
        "cuisine": "Fast Food",
        "rating": 3.9
    }
}

# Update the rating of Pizza Point
restaurants["Pizza Point"]["rating"] = 4.5

print(restaurants)