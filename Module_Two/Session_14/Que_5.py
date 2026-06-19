# Que_5:- Refactor the following code to use dynamic nested dictionary creation so that it doesn't throw a KeyError when adding a new user or playlist:<br><br>playlists = {'user1': {'Favourites': ['Song1', 'Song2']}}<br>playlists['user2']['Chill'].append('Song3')<br><br><em><strong>Hint:</strong> Use collections.defaultdict or check if keys exist before accessing.</em>

playlists = {
    'user1': {
        'Favourites': ['Song1', 'Song2']
    }
}

# Create user if it doesn't exist
if 'user2' not in playlists:
    playlists['user2'] = {}

# Create playlist if it doesn't exist
if 'Chill' not in playlists['user2']:
    playlists['user2']['Chill'] = []

# Add the song
playlists['user2']['Chill'].append('Song3')

print(playlists)