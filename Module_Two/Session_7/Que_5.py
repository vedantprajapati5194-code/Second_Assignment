# Que_5:- Refactor your character count script to use a function named char_count_dict(text) that returns the frequency dictionary, and then print the dictionary sorted by character (A-Z or a-z).

def char_count_dict(text):
    freq = {}

    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq


text = input("Enter a string: ")

result = char_count_dict(text)

# Print dictionary sorted by character
for char in sorted(result):
    print(char, ":", result[char])