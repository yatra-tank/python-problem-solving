# Given array of strings, remove empty strings "".
L1 = eval(input("Enter a list of strings: "))
L2 = []

for i in L1:
    if i == "":
        pass
    else:
        L2.append(i)

print(L2)