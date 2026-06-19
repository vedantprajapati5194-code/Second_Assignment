# Que_2:- Create a program that reads a short review (multi-line string) about your favorite food delivery app (like Zomato or Swiggy) and counts the frequency of each word, displaying the results as a dictionary.<br><br><em><strong>Hint:</strong> Convert all words to lowercase and remove punctuation for accurate counting.</em>

review = """
Zomato is my favorite food delivery app.
Zomato delivers food quickly and the app is easy to use.
The delivery service is good, and the food arrives on time!
"""

# Convert to lowercase
review = review.lower()

# Remove punctuation
for p in ".,!?":
    review = review.replace(p, "")

# Split the text into words
words = review.split()

# Count word frequencies
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the dictionary
print(word_count)
