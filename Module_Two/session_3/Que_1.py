# Que_1:- Given a list of cricket scores: [56.7, 102.3, 88.9, 45.2, 120.8], use the round() function to create a new list with each score rounded to the nearest integer and print both the original and rounded lists.

scores = [56.7, 102.3, 88.9, 45.2, 120.8]

rounded_scores = []

for score in scores:
    rounded_scores.append(round(score))

print("Original scores:", scores)
print("Rounded scores:", rounded_scores)