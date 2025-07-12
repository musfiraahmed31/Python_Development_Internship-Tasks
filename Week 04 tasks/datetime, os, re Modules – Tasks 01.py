import datetime

Year = int(input("Enter your birth year:"))
Month = int(input("Enter your birth month:"))
Day = int(input("Enter your birth day:"))

BirthDate = datetime.date(Year, Month, Day)
Today = datetime.date.today()

AgeYears = Today.year - BirthDate.year

if (Today.month, Today.day) < (BirthDate.month, BirthDate.day):
    AgeYears -= 1

DaysLived = (Today - BirthDate).days

print("\nYou are", AgeYears, "years old.")
print("You have lived for", DaysLived, "days.")
