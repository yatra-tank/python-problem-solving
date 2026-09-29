# Move last element to front.
L = eval(input("Enter an array: "))

if L:
    L.insert(0, L[-1])
    L.pop()

print(L)