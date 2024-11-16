numbers = [1, 2, 3, 4, 5]
numbers_v2 = [numbers[i] * 2 for i in range(0, len(numbers))]
numbers_v3 = list(map(lambda i: i, numbers))
result = list(map(lambda i, j: i + j, numbers_v2, numbers_v3))
print(result)

items = [
    {'title': 'Title 1', 'price': 10},
    {'title': 'Title 2', 'price': 20},
    {'title': 'Title 3', 'price': 30},
    {'title': 'Title 4', 'price': 40},
    {'title': 'Title 5', 'price': 50},
]
items2 = items.copy()
prices = list(map(lambda item: item['price'], items2))