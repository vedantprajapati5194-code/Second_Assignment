# Que_5:- Build a Spotify-style daily playlist shuffle: given a list of 8 song names, use the random module to select and print 3 random songs for today's playlist.<br><br><em><strong>Hint:</strong> Use random.sample() for this task.</em>

import random

# List of 8 songs
songs = [
    "Shape of You",
    "Believer",
    "Perfect",
    "Blinding Lights",
    "Levitating",
    "Stay",
    "Senorita",
    "Bad Habits"
]

# Select 3 random songs
today_playlist = random.sample(songs, 3)

print("Today's Playlist:")
for song in today_playlist:
    print(song)