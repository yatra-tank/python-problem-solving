# Right rotation: last elements move to front.
L = eval(input("Enter a list of numbers: "))
k = int(input("Enter the value of k: "))

k = k % len(L)
L = L[-k:] + L[:-k]

print(L)