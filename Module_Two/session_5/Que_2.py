# Que_2:- Build a nested dictionary called user_profiles where each key is a username (like 'raj_07', 'ananya_xo') and the value is another dictionary with keys: 'followers', 'following', and 'posts'. Add data for at least two users and print the number of followers for 'ananya_xo'.

user_profiles = {
    "raj_07": {
        "followers": 250,
        "following": 180,
        "posts": 45
    },
    "ananya_xo": {
        "followers": 500,
        "following": 300,
        "posts": 75
    }
}

print("Followers of ananya_xo:", user_profiles["ananya_xo"]["followers"])