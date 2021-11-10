import random
mini =1
maxi =6
dice = random.randrange(mini,maxi+1)

if dice ==1:
    print()
    print(' o ')
    print()
elif dice == 2:
    print('  o')
    print()
    print('o')
elif dice == 3:
    print('  o')
    print(' o')
    print('o')
elif dice == 4:
    print('o o')
    print()
    print('o o')
elif dice == 5:
    print('o o')
    print(' o')
    print('o o')
else:
    print('o o')
    print('o o')
    print('o o')
 

print('---------------')

mini1=1
maxi1=6
dice1=[]

for i in range(5):
    dice1.append(random.randint(mini1,maxi1))
    
    

dice1.sort()
print(dice1)
