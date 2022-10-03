import random


def add_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def winner(player_score, computer_score):
    if player_score > 21:
        return 'You went over. You lose'
    elif computer_score > 21:
        return 'You win'

    if player_score > computer_score:
        return 'You win'
    elif player_score == computer_score:
        return 'It\'s a draw'
    else:
        return 'You lose'


def blackjack():
    player_cards = [add_card()]
    player_score = sum(player_cards)

    computer_score = 0
    computer_cards = []

    while computer_score < 16:
        if computer_score == 21:
            return 'You lose'
        computer_cards.append(add_card())
        computer_score = sum(computer_cards)

    # add a new card to player's hand
    draw_a_card = True
    while draw_a_card:
        player_cards.append(add_card())
        player_score = sum(player_cards)

        print(f'\tYour cards: {player_cards} current score: {player_score}')
        print(f'\tComputer\'s first card: {computer_cards[0]}')

        if player_score > 21:
            break
        elif player_score == 21:
            return 'You win'

        new_card = input("Type 'y' to get another card , type 'n' to pass: ")
        if new_card == 'n':
            draw_a_card = False

    # final score
    print(f'\tYour final hand: {player_cards}, final score: {player_score}')
    print(f'\tComputer\'s final hand: {computer_cards}, final score: {computer_score}')
    return winner(player_score, computer_score)