def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def finddays(year,month):
    days_list=[31,28,30,31,30,31,30,31,30,31,30,31]
    if leap_year(year) and month==2:
        return 29
    else:
        return days_list[month-1]


year=int(input("enter year"))
month=int((input("enter month")))
result=finddays(year,month)
print(result)