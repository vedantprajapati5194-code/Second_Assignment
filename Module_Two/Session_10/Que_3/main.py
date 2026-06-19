from playlist import add_song, remove_song

# Create an empty playlist
playlist = []

# Add songs
add_song("Kesariya", playlist)
add_song("Shape of You", playlist)
add_song("Believer", playlist)

print("Playlist before removing a song:")
print(playlist)

# Remove a song
remove_song("Shape of You", playlist)

print("Playlist after removing a song:")
print(playlist)