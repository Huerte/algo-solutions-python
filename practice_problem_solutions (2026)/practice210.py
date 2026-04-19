# HackerRank - Day of the Programmer

def dayOfProgrammer(year):
    if year < 1919:
        days = 243 if year % 4 != 0 else 244
    else:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            days = 244
        else:
            days = 243
    
    if year == 1918:
        days -= 13