# Return True if each element is strictly greater than previous.
L = eval(input("Enter a list of numbers: "))

for i in range(1, len(L)):
    if L[i] <= L[i - 1]:
        print("false")
        break
else:
    print("true")