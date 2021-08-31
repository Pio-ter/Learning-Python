string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for i in range(1,10):
    if i %2==0:
        print(string_A)
    else:
        print(string_B)
    i+=1
    
for i in range(1,10):
    print('x'*i)
    i+=1

for i in range(1,10):
    if i %2==0:
        print('x'*i)
    else:
        print('o'*i)
