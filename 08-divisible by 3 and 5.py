# Given a number, print if it is divisible by both 3 and 5.
n = int(input("Enter a number: "))
if n%3 == 0 and n%5 == 0:
    print("divisible by 3 and 5")
else:
    print("not divisible by 3 and 5")
