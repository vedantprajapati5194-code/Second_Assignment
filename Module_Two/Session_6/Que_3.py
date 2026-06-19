# Que_3:-Suppose you have two lists: one with IPL team names and another with their total points this season. Use zip() to combine them into a dictionary, then print only the teams that have more than 10 points.<br><br><em><strong>Hint:</strong> After creating the dictionary, use a for loop to filter and print.</em>

# List of IPL teams
teams = ["CSK", "MI", "RCB", "GT", "RR"]

# List of points
points = [12, 8, 14, 10, 16]

# Create dictionary using zip()
ipl_points = dict(zip(teams, points))

# Print the dictionary
print("IPL Points Table:")
print(ipl_points)

print("\nTeams with more than 10 points:")

# Filter teams with more than 10 points
for team, point in ipl_points.items():
    if point > 10:
        print(team, "-", point, "points")