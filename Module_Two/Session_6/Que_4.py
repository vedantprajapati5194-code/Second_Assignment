# Que_4:- Given three lists — movie titles, genres, and ratings — use zip() to create a list of dictionaries where each dictionary contains keys 'title', 'genre', and 'rating' for a movie, then print the list.<br><br><em><strong>Constraint:</strong> Do not use any external libraries.</em>

# Lists of movie details
titles = ["Inception", "Titanic", "Avengers"]
genres = ["Sci-Fi", "Romance", "Action"]
ratings = [8.8, 7.9, 8.4]

# Empty list to store movie dictionaries
movies = []

# Use zip() to combine the lists
for title, genre, rating in zip(titles, genres, ratings):
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    movies.append(movie)

# Print the list of dictionaries
print(movies)