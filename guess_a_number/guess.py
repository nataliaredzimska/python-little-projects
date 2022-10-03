# choosing a level
def choose_a_level(level):
    if level == 'easy':
        attempts = 10
    else:
        attempts = 5

    return attempts


# guessing a number
def guess_a_number(attempts, secret_number):
    # play until out of attempts
    while attempts > 0:
        print(f'You have {attempts} attempts remaining to guess the number.')
        guess = int(input('Make a guess: '))

        # when guess is out of valid range
        while guess < 1 or guess > 100:
            print('Invalid input.')
            guess = int(input('Guess again: '))

        # when guess is right
        if guess == secret_number:
            return f'You got it! The answer was {guess}'

        # when guess is wrong
        else:
            if guess > secret_number:
                print('Too high.')
            else:
                print('Too low.')

            attempts -= 1
            if attempts > 0:
                print('Guess again')

    # out of attempts
    else:
        return '0 attempts. You lost.'