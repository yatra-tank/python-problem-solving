# Number is Armstrong if sum of cubes of its digits equals the number (for 3-digit).
n = input("Enter a three- digit number: ")
a = int(n[0])
b = int(n[1])
c = int(n[2])

i = a**3 + b**3 + c**3
if i == int(n):
    print("true")
else:
    print("false")