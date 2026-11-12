# Return the k-th smallest element (1-based index) after sorting.
L = eval(input("Enter a list of elements: "))
k = int(input("Enter a number: "))

L = sorted(L)
print(L[k - 1])