# Que_1:- Write a Python script that takes a string input from the user and prints a dictionary showing how many times each character appears in the string.

text = input("Enter a string: ")

char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)