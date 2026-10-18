# Return true if array contains any value that appears more than once.
L1 = eval(input("Enter a list of numbers: "))
L2 = []

for i in L1:
    if i not in L2:
        L2.append(i)
    else:
        print("true")
else:
    print("false")