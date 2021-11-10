colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]

allCards = []
for color in colors:
    for figure in figures:
        aCard = figure.copy()
        aCard['Color'] = color
        allCards.append(aCard)
import random
random.shuffle(allCards)


player1 = allCards[:12]
player2 = allCards[12:]

print('gracz1: \n', player1, '\ngracz2: \n', player2)

while len(player1) or len(player2) == 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    if card1['Power'] == card2['Power']:
        player1.append(card1)
        player2.append(card2)
        print(card1['Power'], card2['Power'], 'REMIS',)
        print('ilość kart pierwszegro gracza: ', len(player1)*'*')
        print('ilość kart drugiego gracza: ', len(player2)*'*')
        
    elif card1['Power'] > card2['Power']:
        player1.append(card1)
        player1.append(card2)
        print(card1['Power'], card2['Power'], 'WYGRYWA GRACZ NR 1')
        print('ilość kart pierwszegro gracza: ', len(player1)*'*')
        print('ilość kart drugiego gracza: ', len(player2)*'*')
       
    else:
        player2.append(card1)
        player2.append(card2)
        print(card1['Power'], card2['Power'], 'WYGRYWA GRACZ NR 2')
        print('ilość kart pierwszegro gracza: ', len(player1)*'*')
        print('ilość kart drugiego gracza: ', len(player2)*'*')

if len(player1) == 0:
    print('Wojnę wygrał gracz nr 2')
else:
    print('Wojnę wygrał gracz nr 1')
   
