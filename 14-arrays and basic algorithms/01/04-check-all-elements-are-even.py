# Return true if all elements are even numbers.
L1 = eval(input("Enter a list of numbers: "))
L2 = []
count = 0

for i in L1:
    if i%2 != 0:
        L2.append(i)

for i in L2:
    count += 1

if count == 0:
    print("true")
else:
    print("false")