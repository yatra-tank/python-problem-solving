# Given sorted array and, target, return index or -1 if not found.
L = eval(input("Enter a list of numbers: "))
target = int(input("Enter a number: "))

lo, hi = 0, len(L) - 1
found = False

while lo <= hi:
    mid = (lo + hi) // 2

    if L[mid] == target:
        print(mid)
        found = True
        break

    if L[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1

if not found:
    print(-1)