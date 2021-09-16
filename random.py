
import random
'''
print(random.randint(1,100))
print('------------------------')
number1 = random.randint(1,100)
number2 = random.randint(1,100)
counter = 1
print(number1)
print(counter, number2)

while number1 != number2:
    counter+=1
    number2 = random.randint(1,100)
    print('próba nr: ', counter, 'wylosowana liczba: ', number2)
'''

countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]
newList = countries
random.shuffle(newList)
groupNumber = 0

i = 0
for i in range(len(newList)):
    if i % 4 ==0:
        groupNumber+=1
        print('----grupa', groupNumber, '----')
    print(newList[i])
    i+=1
