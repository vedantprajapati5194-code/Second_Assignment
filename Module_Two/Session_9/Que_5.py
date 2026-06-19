# Que_1:- Use ChatGPT to generate a lambda function that takes a string and returns True if it is a palindrome (reads the same forwards and backwards), otherwise False. Test it with 'madam', 'python', and 'noon'.

# Lambda function to check palindrome
is_palindrome = lambda text: text == text[::-1]

# Test strings
words = ["madam", "python", "noon"]

for word in words:
    print(word, "->", is_palindrome(word))