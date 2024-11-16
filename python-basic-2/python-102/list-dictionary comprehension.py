import random
# List comprehension
numbers = []
for element in range(0, 10):
    if element % 2 == 0:
        numbers.append(element)
print(numbers)

numbers2 = [element for element in range(0, 10) if element % 2 == 0]
print(numbers)

# Dictionary comprehension
dict = {}
for i in range(0, 10):
    if i % 2 == 0:
        dict[i] = i * 2
print(dict)

dict2 = {i: i * 2 for i in range(0, 10) if i % 2 == 0}
print(dict2)

set_countries = {'Colombia', 'Venezuela', 'Argentina', 'Peru', 'Chile'}
dict3 = {i: random.randint(1, 100) for i in set_countries}
print(dict3)

names = ['Yamith', 'Luis', 'Carlos']
ages = [25, 30, 35]
dict4 = {names[i] : ages[i] for i in range(0, len(names))}
print(dict4)