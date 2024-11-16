""" import this """

def run(): 
    set_countries = {'Colombia', 'Venezuela', 'Argentina', 'Peru', 'Chile'}
    set_numbers = {1, 2, 3, 4, 5}
    set_types = {1, 'Hello', 3.14, True}
    set_from_string = set('Hello')
    set_from_tuples = set(('abs', 2, 3, 4, 5))
    print(set_from_tuples)

    print(len(set_countries))
    print('Peru' in set_countries)
    set_countries.add('Mexico')
    print(set_countries)
    set_countries.update({'Brasil', 'Uruguay', 'Paraguay'})

    set_countries.remove('Mexico')


data = [
    {
        "Country": "USA",
        "Cases": 100,
    }, {
        "Country": "Mexico",
        "Cases": 200,
    }
]

if __name__ == '__main__':
    run()