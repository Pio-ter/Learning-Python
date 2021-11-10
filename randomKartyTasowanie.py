import random


colors = ['Hearts','Diamonds','Clubs','Spades']
figures = ['Ace','King','Queen','Jack','10','9']
allCards = []
i= 0



for color in colors:
    for figure in figures:
        card = color + figure
        allCards.append(card)
        i+=1
print(allCards)

random.shuffle(allCards)
print(allCards)
'''
player1 = []
player2 = []
maxi = len(allCards)


for i in range(maxi):
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])
print('-----player1-----')        
print('player1: ', player1)
print('-----player2-----')
print('player2: ', player2)
'''

player1 = allCards[:12]
print(player1)
player2 = allCards[12:]
print(player2)

