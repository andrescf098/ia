suma = lambda x,y: x+y
assert suma(2,2) == 4

try:
    print(0/0)
except ZeroDivisionError as error:
    print(error)
