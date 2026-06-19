# Que_3:- Given the following string: 'Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match', write a function word_freq_dict(text) that returns a dictionary with the frequency of each word.

def word_freq_dict(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    for p in ",.!?":
        text = text.replace(p, "")

    # Split into words
    words = text.split()

    # Count frequencies
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


text = "Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match"

result = word_freq_dict(text)
print(result)