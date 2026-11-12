# Return the k-th largest element (1-based index) after sorting.
L = eval(input("Enter a list of elements: "))
k = int(input("Enter a number: "))

L.sort(reverse=True)
print(L[k - 1])