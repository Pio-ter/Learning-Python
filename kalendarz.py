
from datetime import datetime

from calendar import monthrange, weekheader, weekday

from sys import stdout


def cal(year=datetime.today().year, month=datetime.today().month):
    """
    Prints month calendar for given year and month.
    """

    this_year = year
    this_month = month

    # number of all days in month
    days_in_month = monthrange(this_year, this_month)[1]

    # which week day is the first day of month
    first_day_of_month = weekday(this_year, this_month, 1)

    # prints header of calendar (width 5)
    print(weekheader(5))

    # positioning loop
    # for proper position of the first element
    for i in range(first_day_of_month):
        stdout.write(6 * ' ')

    i = 1
    while i <= days_in_month:
        stdout.write(' {:>2}   '.format(i))
        # new line if sunday
        if weekday(this_year, this_month, i) == 6:
            print('')
        i += 1
    print('')

if __name__ == '__main__':
    cal()
