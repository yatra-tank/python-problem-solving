# Assume array has at least 2 distinct elements.
L = eval(input("Enter an array: "))

n = min(L)
index = L.index(n)
L.pop(index)

print(min(L))