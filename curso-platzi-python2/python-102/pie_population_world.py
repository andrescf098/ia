from read_csv import read_csv
import plot

def run():
    path = "D:/Programacion/IA/curso-platzi-python2/python-102/files/world_population.csv"
    data = read_csv(path)
    data = list(filter(lambda x: x['Continent'] == 'South America', data))
    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    plot.generate_pie_chart(countries, percentages)

if __name__ == '__main__':
    run()
