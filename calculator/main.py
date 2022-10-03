# source: https://www.udemy.com/course/100-days-of-code/

from art import logo
from calc import calc

# logo
print(logo)

# start
first_number = float(input('What\'s the first number? '))
restart = True

while restart:
    print('+')
    print('-')
    print('*')
    print('/')

    operation = input('Pick an operation: ')
    second_number = float(input('What\'s the next number? '))

    output = calc(first_number, second_number, operation)
    # print(type(output))
    if output != 'invalid input':
        if second_number != 0:
            print(f'{first_number} {operation} {second_number} = {output}')
        else:
            print(output)
    else:
        print('Invalid input.')

    if_replay = input(f'Type \'y\' to continue calculating with {output}, or type \'n\' to start a new calculation.\n')
    if if_replay == 'n':
        output = 0
        first_number = float(input('What\'s the first number? '))
    elif if_replay == 'y':
        if type(output) != float:
            output = first_number
        first_number = output
    else:
        print('Invalid input.')
        print('Goodbye.')
        break
        