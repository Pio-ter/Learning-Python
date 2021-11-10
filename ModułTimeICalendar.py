import time
print(time.time())
print(time.localtime(time.time()))
import calendar

print(calendar.month(2001,9, w=5, l=3))

calendar.setfirstweekday(6)
print(calendar.month(1988,11, w=5, l=3))

print(calendar.isleap(2000))

print(calendar.calendar(2021))
