# Que_2:- Write a function add_song_to_playlist(playlists, user, playlist_name, song_title, artist) that adds a song to a user's playlist in a nested dictionary structure like Spotify. If the user or playlist doesn't exist, create them dynamically.

def add_song_to_playlist(playlists, user, playlist_name, song_title, artist):
    # Create the user if it doesn't exist
    if user not in playlists:
        playlists[user] = {}

    # Create the playlist if it doesn't exist
    if playlist_name not in playlists[user]:
        playlists[user][playlist_name] = []

    # Add the song to the playlist
    playlists[user][playlist_name].append({
        "title": song_title,
        "artist": artist
    })


# Empty dictionary to store playlists
playlists = {}

# Add songs
add_song_to_playlist(playlists, "Rahul", "Favorites", "Shape of You", "Ed Sheeran")
add_song_to_playlist(playlists, "Rahul", "Favorites", "Blinding Lights", "The Weeknd")
add_song_to_playlist(playlists, "Priya", "Workout", "Believer", "Imagine Dragons")
add_song_to_playlist(playlists, "Priya", "Workout", "Thunder", "Imagine Dragons")

# Print the playlists
print(playlists)
