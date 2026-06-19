# Que_1:-Create a Python dictionary called playlist with three songs as keys and their durations (in seconds) as values. Update the duration of one song and print the updated dictionary.

playlist = {
    "Shape of You": 240,
    "Believer": 204,
    "Senorita": 191
}

# Update the duration of a song
playlist["Believer"] = 210

print("Updated playlist:")
print(playlist)