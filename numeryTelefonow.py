import random

rNumber = '{0:003d}-{1:003d}-{2:003d}'
i = 0
while i <= 100:
    print(rNumber.format(random.randint(500,600), random.randint(0,1000),random.randint(0,1000)))
    i+=1
