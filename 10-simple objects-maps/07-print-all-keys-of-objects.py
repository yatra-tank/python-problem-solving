# Given object, return array of keys.
d = {}
L = []

n = int(input("Enter number of entries: "))

for i in range(n):
    k = input("Enter your key value: ")
    v = input("Enter your value: ")

    d[k] = v

for i in d:
    L.append(i)

print(L)