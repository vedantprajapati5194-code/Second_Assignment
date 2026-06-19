# Que_1:- Use list comprehension to generate a list of all even numbers between 10 and 50 (inclusive).

even_numbers = [num for num in range(10, 51) if num % 2 == 0]

print(even_numbers)