from trace import Trace

__author__ = 'markchan'


def nextDay(year, month, day):
    if day < 30:
        return year, month, day + 1

    elif month < 12:
        return year, month + 1, 1
    else:
        return year + 1, 1, 1


print nextDay(1999, 2, 10)


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    elif year1 == year2:
        if month1 < month2:
            return True
        elif month1 == month2:
            return day1 < day2
    else:
        return False


print dateIsBefore(1999, 2, 1, 1999, 2, 11)


def daysBetweenDates(year_01, month_01, day_01, year_02, month_02, day_02):
    days = 0
    while dateIsBefore(year_01, month_01, day_01, year_02, month_02, day_02):
        year_01, month_01, day_01 = nextDay(year_01, month_01, day_01)
        days += 1

    return days


def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def daysInMonth(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    if month == 2:
        if isLeapYear(year):
            return 29
        return 28
    else:
        return 30


print daysInMonth(2012,4)

print 'leap year',
print isLeapYear(2012)

# def daysBetweenDates(year1, month1, day1, year2, month2, day2):
# """Returns the number of days between year1/month1/day1
# and year2/month2/day2. Assumes inputs are valid dates
# in Gregorian calendar."""
# # program defensively! Add an assertion if the input is not valid!
#
# days = 0
# while dateIsBefore(year1, month1, day1, year2, month2, day2):
# year1, month1, day1 = nextDay(year1, month1, day1)
# days += 1
# return days


print daysBetweenDates(1999, 2, 1, 1999, 12, 13)