# Que_1:-  Create a Python list called playlist containing five of your favorite song names, then use a for loop to print each song with its position in the playlist (starting from 1).

playlist = [
    "die with a smile",
    "siyaara",
    "all is well",
    "kesariya",
    "Sahiba"
]

position = 1

for song in playlist:
    print(position, "-", song)
    position = position + 1