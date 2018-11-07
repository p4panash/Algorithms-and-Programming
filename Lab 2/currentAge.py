import datetime
from datetime import date


def GetYear(date):
    return int(str(date)[:4])


def GetMonth(date):
    return int((str(date)[5:])[:2])


def GetDay(date):
    return int((str(date)[8:])[:2])


def GetNumberOfDays(month):
    if month == 1:
        return 31
    elif month == 2:
        return 28
    elif month == 3:
        return 31
    elif month == 4:
        return 30
    elif month == 5:
        return 31
    elif month == 6:
        return 30
    elif month == 7:
        return 31
    elif month == 8:
        return 31
    elif month == 9:
        return 30
    elif month == 10:
        return 31
    elif month == 11:
        return 30
    elif month == 12:
        return 31


def DaysBetweenMonths(firstMonth, secondMonth):
    days = 0
    if firstMonth < secondMonth:
        for month in range(firstMonth, secondMonth + 1):
            days += GetNumberOfDays(month)
    else:
        for month in range(secondMonth, firstMonth + 1):
            days += GetNumberOfDays(month)
    return days


def CountLeapYears(birthdate, currentTime):
    count = 0
    for year in range(GetYear(birthdate), GetYear(currentTime) + 1):
        if year % 4 == 0:
            count += 1
    return count


def GetAgeInDays(birthdate, currentTime):
    days = GetDay(currentTime) - GetDay(birthdate)
    days += DaysBetweenMonths(GetMonth(birthdate), 12) + DaysBetweenMonths(1, currentTime.month - 1)
    days += CountLeapYears(birthdate, currentTime)
    days += (GetYear(currentTime) - GetYear(birthdate) - 1) * 365
    if GetMonth(birthdate) > 2:
        days -= 1
    return days


def main() :
    birthdate = input("Introduce birthdate: ")
    currentTime = datetime.datetime.now().date()
    print(str(GetAgeInDays(birthdate, currentTime)))
    #the easiest method
    givenDate = date(GetYear(birthdate), GetMonth(birthdate), GetDay(birthdate))
    print((currentTime - givenDate).days)


main()