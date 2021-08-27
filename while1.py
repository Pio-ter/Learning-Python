###
firstRow=1
lastRow=31
currentRow=firstRow

while currentRow<=lastRow:
    print('Row number', currentRow)
    currentRow+=1
else:
    print('full')

firstNum=1
lastNum=13

while firstNum<=lastNum:
    print(firstNum, '.', 'Kwadrat tej liczby to:', firstNum**2,', sześcian tej liczby to', firstNum**3)
    firstNum+=1
else:
    print('end of counting')
###

fNum=0
lNum=16
while fNum<=lNum:
    print('2 do potęgi', fNum, 'to:', 2**fNum)
    fNum+=1
else:
    print('koniec')

a=1
b=10
while a<=b:
    print(a*'x')
    a+=1
