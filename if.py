minLikes = 500
minShares = 100
numLikes= 501
numShares=90
if numLikes>=minLikes and numShares>=minShares:
    print('Price is 10% lower')
else:
    if numLikes<minLikes:
        print('not enaugh likes')
    else:
        print('not enaugh shares')
        

isPizzaOrdered=True
isBigDrinkOrdered=True
isWeekend=False

if (isPizzaOrdered or isBigDrinkOrdered)and not isWeekend:
    print('Kupon na burgera')
else:
    print('Kupuj dalej')

diskSize=140
diskSizeUsed=129
fileSize=10

if (diskSize-diskSizeUsed)>=10:
    print("file can be downlowaded")
else:
    print("not enaugh space")
