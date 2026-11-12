# Left rotation: first elements move to end.
L = eval(input("Enter a list of numbers: "))
k = int(input("Enter the value of k: "))

k = k % len(L)
L = L[k:] + L[:k]

print(L)