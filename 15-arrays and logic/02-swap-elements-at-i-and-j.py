# Given an array and two indices i and j, swap elements at those indices.
L = eval(input("Enter a list of numbers: "))
i = int(input("Enter the index i: "))
j = int(input("Enter the index j: "))

L[i], L[j] = L[j], L[i]

print(L)