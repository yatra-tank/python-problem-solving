# Return an object where key = number, value = count
L = eval(input("Enter a array: "))
dict = {}

for i in L:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)