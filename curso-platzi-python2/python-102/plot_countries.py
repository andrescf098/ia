import csv
import plot

def read_csv(path):
    country_input = input("Enter the country: ")
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        find_country = list(filter(lambda country: country['Country/Territory'] == country_input.lower().capitalize(), data))[0]
        filtered_data = {key.replace(" Population", ""): value for key, value in find_country.items() if "Population" in key}
        del filtered_data['World Percentage']
        sorted_data = {key: filtered_data[key] for key in sorted(filtered_data, key=lambda x: int(x))}
        return sorted_data

if __name__ == '__main__':
    data = read_csv("D:/Programacion/IA/curso-platzi-python2/python-102/files/world_population.csv")
    values = list(data.values())
    values = [int(value) for value in values]
    plot.generate_bar_char(list(data.keys()), values)