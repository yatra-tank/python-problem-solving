# Using a frequency object, return the number with highest count.
L = eval(input("Enter a array: "))
dict = {}

for i in L:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

n = max(dict.values())

for i in dict:
    if dict[i] == n:
        print(i)
        break