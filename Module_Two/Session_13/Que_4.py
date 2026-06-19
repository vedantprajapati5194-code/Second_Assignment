# Que_4:- Given a matrix representing ratings for 3 Zomato restaurants by 4 users (e.g., [[4, 5, 3, 2], [5, 4, 4, 3], [3, 2, 5, 5]]), use a nested list comprehension to find all ratings above 4 and flatten them into a single list.<br><br><em><strong>Hint:</strong> You will need two for loops inside the list comprehension to flatten the matrix.</em>

ratings = [
    [4, 5, 3, 2],
    [5, 4, 4, 3],
    [3, 2, 5, 5]
]

high_ratings = [rating for row in ratings for rating in row if rating > 4]

print(high_ratings)