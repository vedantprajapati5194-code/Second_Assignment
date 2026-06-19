# Que_3:- Use a lambda function with the filter() function to get only the usernames with more than 1000 followers from this list: [('raj', 800), ('simran', 1500), ('veer', 1200), ('ananya', 950)]. Print the usernames that would get the 'K' badge like Instagram.

# List of usernames and followers
users = [
    ('raj', 800),
    ('simran', 1500),
    ('veer', 1200),
    ('ananya', 950)
]

# Filter users with more than 1000 followers
k_badge_users = filter(lambda user: user[1] > 1000, users)

print("Users with K badge:")

for username, followers in k_badge_users:
    print(username)