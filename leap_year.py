#Given a year, return True if it is a leap year, else return False

def is_leap_year_1(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        
def is_leap_year_2(year):
    # if (year is not divisible by 4) then (it is a common year)
    if year % 4:
        return False
    # else if (year is not divisible by 100) then (it is a leap year)
    if year % 100:
        return True
    # else if (year is not divisible by 400) then (it is a common year)
    if year % 400:
        return False
    # else (it is a leap year)
    return True
    
def is_leap_year_3(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
year=int(input("Input a year:"))
print(f"Is leap year with  first  way: {is_leap_year_1(year)}")
print(f"Is leap year with secound way: {is_leap_year_2(year)}")
print(f"Is leap year with  third  way: {is_leap_year_3(year)}")
