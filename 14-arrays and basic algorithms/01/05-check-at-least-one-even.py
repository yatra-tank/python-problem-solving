# Return true if at least one element is even.
L = eval(input("Enter a list of numbers: "))

for i in L:
    if i%2 == 0:
        print("true")
        break
else:
    print("false")