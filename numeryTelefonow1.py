import random

rNumber = '{0:003d}-{1:003d}'
rNumber1 = 500
i = 0
x = 500
while i <= 100:
    while rNumber1 >=500 and rNumber1 < 600:
        rNumber1+=1
        print(rNumber1, '-', rNumber.format(random.randint(0,1000),random.randint(0,1000)))
    i+=1
   
