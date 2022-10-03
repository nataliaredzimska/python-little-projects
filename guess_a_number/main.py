# source: https://www.udemy.com/course/100-days-of-code/

from random import randint
from art import logo
from guess import guess_a_number, choose_a_level


# WELCOME
print(logo)

print('Welcome to the Number Guessing Game!')
print('I\'m thinking of a number between 1 and 100.')


# selecting a secret number
secret_number = randint(1, 101)
# print(f'Psst, the secret number is {secret_number}')


# choose a level
chosen_level = input('Choose a difficulty. Type \'easy\' or \'hard\': ').lower()


# play the game
result = guess_a_number(choose_a_level(chosen_level), secret_number)
print(result)
