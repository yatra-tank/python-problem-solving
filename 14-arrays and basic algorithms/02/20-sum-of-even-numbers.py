# Return sum of only even numbers.
L1 = eval(input("Enter a list of strings: "))

L2 = []
sum = 0

for i in L1:
    if i%2 == 0:
        L2.append(i)

for j in L2:
    sum += j

print(sum)