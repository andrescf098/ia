import csv

def read_csv(path):
   total = 0
   with open(path, 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter=",")
      for row in reader:
         total += int(row[len(row) - 1])
   return total

if __name__ == '__main__':
    total = read_csv("D:/Programacion/IA/curso-platzi-python2/python-102/files/data.csv")
    print(total)