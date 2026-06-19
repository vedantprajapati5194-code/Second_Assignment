from playlist import add_song, remove_song, display_playlist

# Create an empty playlist
playlist = []

# Add songs
add_song("Kesariya", playlist)
add_song("Shape of You", playlist)
add_song("Believer", playlist)

print("After adding songs:")
display_playlist(playlist)

# Remove a song
remove_song("Shape of You", playlist)

print("\nAfter removing 'Shape of You':")
display_playlist(playlist)