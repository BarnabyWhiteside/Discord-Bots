import random
import os

def calcHand(hand):
    sum = 0

    nonAces = [card for card in hand if card != 'A']
    Aces = [card for card in hand if card == 'A']

    for card in nonAces:
        if card in 'JQK':
            sum += 10
        else:
            sum +=int(card)

    for card in Aces:
        if sum <= 10:
            sum += 11
        else:
            sum += 1

    return sum

cards = [
    '2','3','4','5','6','7','8','9','10','J','Q','K','A',
    '2','3','4','5','6','7','8','9','10','J','Q','K','A',
    '2','3','4','5','6','7','8','9','10','J','Q','K','A',
    '2','3','4','5','6','7','8','9','10','J','Q','K','A'
]

random.shuffle(cards)

dealer = []
player = []

player.append(cards.pop())
dealer.append(cards.pop())
player.append(cards.pop())
dealer.append(cards.pop())

standing = False
firstHand = True

while True:
    os.system('cls')

    playerScore = calcHand(player)
    dealerScore = calcHand(dealer)

    if standing:
        print('Dealer Cards: [{}] ({})'.format(']['.join(dealer), dealerScore))
    else:
        print('Dealer Cards: [{}][?]'.format(dealer[0]))

    print('Player Cards: [{}] ({})'.format(']['.join(player), playerScore))
    print('')

    if standing:
        if dealerScore > 21:
            print('Dealer busts')
        elif playerScore == dealerScore:
            print('Push')
        elif playerScore > dealerScore:
            print('Player wins')
        else:
            print('Dealer wins')

        break

    if firstHand and playerScore == 21:
        print('Blackjack')
        break

    if playerScore > 21:
        print('Player bust')
        break

    print('What would you like to do?')
    print(' [1] Hit')
    print(' [2] Stand')
    choice = input('\n')

    if choice == '1':
        player.append(cards.pop())
    elif choice == '2':
        standing = True
        while calcHand(dealer) <= 16:
            dealer.append(cards.pop())
