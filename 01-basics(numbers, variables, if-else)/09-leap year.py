# Given a year, check if it is a leap year. (Simple version: divisible by 4 → leap; you can refine later.)
n = int(input("Enter year:"))
if n % 4 == 0:
    if n % 100 == 0:
        if n % 400 == 0:
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:
    print("not a leap year")
