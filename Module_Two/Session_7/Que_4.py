# Que_4:- Modify your word frequency program to ignore common stopwords like 'the', 'and', 'in', 'of', 'a', 'to', 'is' when counting word frequencies.<br><br><em><strong>Constraint:</strong> Use a list of stopwords and filter them out before counting.</em>

def word_freq_dict(text):
    # List of stopwords
    stopwords = ["the", "and", "in", "of", "a", "to", "is"]

    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    for p in ",.!?":
        text = text.replace(p, "")

    # Split into words
    words = text.split()

    # Dictionary to store frequencies
    freq = {}

    for word in words:
        # Skip stopwords
        if word in stopwords:
            continue

        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


text = "Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match"

result = word_freq_dict(text)
print(result)