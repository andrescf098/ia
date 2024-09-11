import random

computer_wins = 0
user_wins = 0
rounds = 1

def home(computer_wins, user_wins, rounds):
    options = ('piedra', 'papel', 'tijera')
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('computer_wins', computer_wins)
    print('user_wins', user_wins)

    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    
    if not user_option in options:
      print('esa opcion no es valida')
      home(computer_wins, user_wins, rounds)
    rounds += 1
    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)
    if user_option == computer_option:
        empate()
    elif user_option == 'piedra':
        piedra(computer_option)
    elif user_option == 'papel':
        papel(computer_option)
    elif user_option == 'tijera':
        tijera(computer_option)
    if computer_wins == 2:
      return print('El ganador es la computadora')

    if user_wins == 2:
      return print('El ganador es el usuario')
    
def empate():
    print('Empate!')

def piedra(computer_option):
    if computer_option == 'tijera':
        print('piedra gana a tijera')
        print('user gano!')
        user_wins += 1
    else:
        print('Papel gana a piedra')
        print('computer gano!')
        computer_wins += 1

def papel(computer_option):
    if computer_option == 'piedra':
        print('papel gana a piedra')
        print('user gano')
        user_wins += 1
    else:
        print('tijera gana a papel')
        print('computer gano!')
        computer_wins += 1

def tijera(computer_option):
    if computer_option == 'papel':
        print('tijera gana a papel')
        print('user gano!')
        user_wins += 1
    else:
        print('piedra gana a tijera')
        print('computer gano!')
        computer_wins += 1

home(computer_wins, user_wins, rounds)
