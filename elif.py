minLikes = 500
minShares = 100
numLikes= 400
numShares=101
if numLikes>=minLikes and numShares>=minShares:
    print('Price is 10% lower')
elif numLikes<minLikes:
    print('not enaugh likes')
else:
    print('not enaugh shares')
    
    
        
isPizzaOrdered=True
isBigDrinkOrdered=False
isWeekend=True
if (isPizzaOrdered or isBigDrinkOrdered)and not isWeekend:
    print('Kupon na burgera')
elif isWeekend:
        print('promo tylko w dni powszednie')
else:
    print('kup pizze lub napój')
    
