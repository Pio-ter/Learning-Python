name='Edek'
age=35
daysInYear=365
message='{0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format (name, age, age*daysInYear))
number=1234567890
number1=12345
number2=number//number1
number3=number%number1
message1='{0:d} divided by {1:d} is {2:d} and the rest is {3:d}'
print(message1.format (number, number1, number2, number3))
print('1234567890 divided by 12345 is', 1234567890//12345, 'and the rest is', 1234567890%12345)
