import functools

numbers = [1, 2, 3, 4, 5]
result = functools.reduce(lambda i, number: i + number, numbers)
result1 = sum(numbers)
print(result, result1)