# Find largest positive and smallest negative (if they exist).
L = eval(input("Enter an array: "))

if max(L) > 0:
    print("Largest postive: ", max(L))
else:
    print("null")

if min(L) < 0:
    print("Smallest negative: ", min(L))
else:
    print("null")