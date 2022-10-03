# source: https://www.udemy.com/course/100-days-of-code/

from func import blackjack
from art import logo

# START A GAME
if_play = input("Do you want to play a Blackjack? Type 'y' or 'n': ")

print(logo)

while if_play == 'y':
    result = blackjack()
    print(result)
    if_play = input("Do you want to play? Type 'y' or 'n': ")
else:
    print('Goodbye.')


## WHAT SHOULD I ADD:
# blackjack (ace + 10)
# if total_score > 21: ace = 1

