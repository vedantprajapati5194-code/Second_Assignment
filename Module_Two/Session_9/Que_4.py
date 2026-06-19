# Que_4:- Create a lambda function that takes two numbers and returns their sum and product as a tuple. Use it to process the pairs (3, 4), (5, 2), and (7, 8).<br><br><em><strong>Hint:</strong> You can return multiple values from a lambda by returning a tuple: (a+b, a*b).</em>

# Lambda function that returns sum and product
calculate = lambda a, b: (a + b, a * b)

# Process the given pairs
pairs = [(3, 4), (5, 2), (7, 8)]

for a, b in pairs:
    result = calculate(a, b)
    print(f"Numbers: {a}, {b}")
    print("Sum =", result[0])
    print("Product =", result[1])
    print()