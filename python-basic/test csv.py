import csv

file_path = "curso-platzi-python/files/products_updated.csv"

""" with open(file_path, mode="r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row) """

new_product = {
    "name": "Mouse", 
    "price": 9.99, 
    "quantity": 50,
    "brand": "ChargerMaster",
    "categoty": "Accesories",
    "entry_date": "2024-07-01"
}

""" with open(file_path, mode="r") as file:
    for row in csv.reader(file):
        print(f"Product: {row['name']}, Price: {row['price']}, Quantity: {row['quantity']}")

with open(file_path, mode="a") as file:
    csv_writer = csv.DictWriter(file, fieldnames=new_product.keys())
    csv_writer.writerow(new_product) """

list = [x for x in range(1,10) if x % 2 != 0 ]
print(list)
n = int('diez')