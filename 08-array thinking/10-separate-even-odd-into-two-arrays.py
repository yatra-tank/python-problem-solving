# Given an array, return two arrays: evens and odds.
L = eval(input("Enter an array: "))
odd = []
even =[]

for i in L:
    if i%2 != 0:
        odd.append(i)
    else:
        even.append(i)

print(f"evens: {even}, odds: {odd}")