# Return true if each element is >= previous one.
L = eval(input("Enter an array: "))

if L == sorted(L):
    print("true")
else:
    print("false")