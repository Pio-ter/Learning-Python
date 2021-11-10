import math

inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02,0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

minvalue = 0
maxvalue = 0
miniinteger = 0
maxiinteger = 0
i = 0
'''
print('długość inputdata: ', len(inputdata))
print('długosć factortable: ', len(factortable))

if len(inputdata) == len(factortable):
    while i < len(inputdata):
        minvalue = inputdata[i]-factortable[i] * inputdata[i]
        maxvalue = inputdata[i]+factortable[i] * inputdata[i]
        print('minvalue: ', minvalue, 'maxvalue: ', maxvalue)
        miniinteger = math.floor(minvalue)
        maxiinteger = math.ceil(maxvalue)
        print(miniinteger, inputdata[i], maxiinteger) 
        i+=1
else:
    print('inputdata and factortable need to have equal number of elements')

print('------------------')

import random


while i < len(inputdata):
    minvalue = inputdata[i]-random.random() * inputdata[i]
    maxvalue = inputdata[i]+random.random() * inputdata[i]
    print('minvalue: ', minvalue, 'maxvalue: ', maxvalue) 
    i+=1
'''

import datetime
print(datetime.date.today().strftime('%Y-%m-%d'))
