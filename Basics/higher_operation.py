# Example function to be applied
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]

# Using map to apply the square function to all items
squared_numbers = map(square, numbers)

print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

# Using map with a lambda function
squared_numbers_lambda = map(lambda x: x * x, numbers)

print(list(squared_numbers_lambda))  # Output: [1, 4, 9, 16, 25]



# Example function to filter even numbers
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Using filter to apply the is_even function
even_numbers = filter(is_even, numbers)

print(list(even_numbers))  # Output: [2, 4, 6, 8]

# Using filter with a lambda function
even_numbers_lambda = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers_lambda))  # Output: [2, 4, 6, 8]



# Lambda function to add two numbers
add = lambda x, y: x + y

print(add(2, 3))  # Output: 5

# Using lambda with map
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x * x, numbers)

print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]



