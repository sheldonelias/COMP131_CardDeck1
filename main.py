import random

# 4 lists of strings initialized
spades = ['A-Sp', '2-Sp','3-Sp','4-Sp','5-Sp','6-Sp','7-Sp','8-Sp','9-Sp','10-Sp','J-Sp','Q-Sp','K-Sp']
hearts = ['A-He', '2-He','3-He','4-He','5-He','6-He','7-He','8-He','9-He','10-He','J-He','Q-He','K-He']
diamonds = ['A-Di', '2-Di','3-Di','4-Di','5-Di','6-Di','7-Di','8-Di','9-Di','10-Di','J-Di','Q-Di','K-Di']
clubs = ['A-Cl', '2-Cl','3-Cl','4-Cl','5-Cl','6-Cl','7-Cl','8-Cl','9-Cl','10-Cl','J-Cl','Q-Cl','K-Cl']
# list of lists initialized
master_deck = [spades, hearts, diamonds, clubs]

deck = master_deck.copy()

print(str(deck[0]) + '\n' + str(deck[1]) + '\n' + str(deck[2]) + '\n' + str(deck[3]) )

'''
Desired Card

desired_card = input()

for suit in deck:
    for current_card in suit:
        if current_card == desired_card:
                print('We found', desired_card )
                
'''

'''
Deal a Hand of Four Cards
'''
# Creates empty hand
hand = []
# Starts with no loops counted
count = 0
# Run a loop while count is less than length of deck, which is 4 suits in length
while( count < len(deck) ):
    # Prints the count
    print(count)
    # Randomly selects a suit and a rank.
    random_suit = random.randint(0, 3)
    # random.randint is inclusive at upper bound!
    # Use len(deck[random_suit-1] as each suit shrinks in length
    random_rank = random.randint(0, len(deck[random_suit])-1)

    # Prevents same card from being requested more than once
    for card in hand:
        if len(hand) > 0:
            if card == master_deck[random_suit][random_rank]:
                print('A duplicate card was randomly selected.')
                # Sets count back one since a dupe was selected
                print('Loop will run again.')
                count -= 1
                # Re-runs loop due to dupe
                continue

    # Prints the selected card
    print( 'random_suit:', random_suit,  'random_rank: ',   random_rank)
    print(deck[random_suit][random_rank])

    # Copies card from deck to hand
    hand.append(deck[random_suit][random_rank])
    # Removes card from deck
    deck[random_suit].remove(deck[random_suit][random_rank])

    # Increments count
    count += 1

print(str(deck[0]) + '\n' + str(deck[1]) + '\n' + str(deck[2]) + '\n' + str(deck[3]) )

print(hand)