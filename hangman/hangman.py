# source: https://www.udemy.com/course/100-days-of-code/

import random, os, sys
from art import title, HANGMANPICS, win, game_over


words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()


# choosing an entry
word = random.choice(words)
secret_word = ['_ ' for x in word]

# for game flow
lose_count = 0
win_count = 0
restart = 1


# INTRO
print(title)

print('Tip: This is an animal.\n\n')

while restart == 1:
    print(''.join(secret_word))
    # print(entry)

    while lose_count < len(HANGMANPICS):
        # when an user guessed a word 
        if win_count == len(word):
            print(win)
            break

        else:
            # GAME
            user_guess = input('Entry a letter: ').lower()

            # if guess is right
            if user_guess in word:
                if user_guess in secret_word:
                    print('You already guessed it. Try something different!\n')

                else:
                    index = 0
                    for x in word:
                        if x == user_guess:
                            secret_word[index] = x
                            win_count += 1
                            # print(f'win_count: {win_count}')
                        index += 1

                    print('\n' + 'WORD: ' + ''.join(secret_word))
                    print('You guessed right.')
                    print('-' * 17 + '\n')

            # if guess is wrong
            else:
                print(f'You lose. \'{user_guess}\' is not in a word.')
                # drawing hangman pic in every lose round
                print(HANGMANPICS[lose_count] + '\n')
                print(''.join(secret_word))
                lose_count += 1

    else:
        # when hangman is hanging
        print(game_over)

    # restarting a game
    if input('Run again? (y/n): ').lower() == 'y':
        restart = 1

        # resetting variables
        word = random.choice(words)
        secret_word = ['_ ' for x in word]
        lose_count = 0
        win_count = 0

        print('*' * 20 + '\n')
        
    else:
        restart = 0

else:
    print('Goodbye.')
