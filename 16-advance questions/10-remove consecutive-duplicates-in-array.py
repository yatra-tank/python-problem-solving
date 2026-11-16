# Given array, keep first of each group of same element, remove consecutive repeats.
L = eval(input("Enter a list: "))

if len(L) == 0:
    print([])
else:
    result = [L[0]]  

    for i in range(1, len(L)):
        if L[i] != L[i - 1]:
            result.append(L[i])

    print(result)