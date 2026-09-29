# Move first element to end.
L = eval(input("Enter an array: "))

if L:
    L.insert(-1, L[0])
    L.pop(0)

print(L)