helloMessage='Hello %s!'
print(helloMessage %('Kate'))
print(helloMessage %('Chris'))
helloMessage='Hello {0:s}!'
print(helloMessage.format ('Kate'))
print(helloMessage.format ('Chris'))
helloMessage='%s has %d %s'
print(helloMessage % ('Kate', 1, 'animal'))
print(helloMessage % ('Chris', 100000, '$'))
helloMessage='{0:s} has {1:d} {2:s}'
print(helloMessage.format ('Kate', 1,'animal'))
print(helloMessage.format('Chris', 100000,'$'))
line='{0:20s} costs {1:6d} €'
print(line.format ('ice cream', 3))
print(line.format ('woda', 30))
print(line.format ('komputer', 11))
