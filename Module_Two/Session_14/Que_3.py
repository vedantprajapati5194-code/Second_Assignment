# Que_3:- Build a dynamic nested dictionary to store IPL cricket match scores: for each team, store a dictionary of player names and their runs. Add at least two teams with three players each, then print the runs scored by a specific player of your choice.

# Create an empty dictionary
ipl_scores = {}

# Add Team CSK
ipl_scores["CSK"] = {
    "Dhoni": 45,
    "Ruturaj": 72,
    "Jadeja": 30
}

# Add Team MI
ipl_scores["MI"] = {
    "Rohit": 65,
    "Surya": 88,
    "Hardik": 40
}

# Print the entire dictionary
print("IPL Scores:")
print(ipl_scores)

# Print runs of a specific player
print("\nRuns scored by Rohit:")
print(ipl_scores["MI"]["Rohit"])