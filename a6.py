year = int(input("Enter year to check if a year is Leap year : "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year! ")
