# Que_1:- Write a lambda function to calculate the square of a number and use it to print the squares of numbers from 1 to 5.

# Lambda function to calculate square
square = lambda x: x * x

# Print squares from 1 to 5
for i in range(1, 6):
    print("Square of", i, "=", square(i))