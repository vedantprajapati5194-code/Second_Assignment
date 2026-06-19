# Que_2:- Write a loop that takes two lists: usernames and their follower counts, and manually creates a dictionary (without using zip()) that maps each username to its follower count, similar to how Instagram tracks followers.

# List of usernames
usernames = ["vedant", "ankit", "milan", "keval"]

# List of follower counts
followers = [1200, 3500, 2100, 5000]

# Empty dictionary
instagram_followers = {}

# Loop through the lists
for i in range(len(usernames)):
    instagram_followers[usernames[i]] = followers[i]

# Print the dictionary
print(instagram_followers)