year = int(input("Enter the year : "))

# Leap Year Calculator (Nested Condition)
if (year % 4 == 0) :
    if (year % 100 == 0) :
        if (year % 400 == 0) :
            print(f"{year} is a leap year")
        else :
            print(f"{year} is not a leap year")
    else :
        print(f"{year} is a leap year")
else :
    print(f"{year} is not a leap year")


# Leap Year Calculator (Logical Operators)
if (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year")
elif (year % 400 == 0 and year % 100 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")