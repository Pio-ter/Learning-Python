import random
my_number=random.randint(0,20)
guess=-1
trials=0
print('Guess my number!')

while guess != my_number:
    guess=int(input())
    trials+=1
    if guess == my_number:
        print('congratulations ' 'number of trials =', trials)
    elif guess>my_number:
        print('my number is smaller')
    else:
        print('my number is greater')
    
