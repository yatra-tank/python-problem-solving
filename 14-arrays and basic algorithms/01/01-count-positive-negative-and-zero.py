# Given an array of numbers, count how many are positive, negative, and zero.
L = eval(input("Enter a list of numbers: "))

count_p = 0
count_n = 0
count_z = 0

for i in L:
    if i > 0:
        count_p += 1
    elif i < 0:
        count_n += 1
    else:
        count_z += 1

print(f"positives: {count_p}, negatives: {count_n}, zeroes: {count_z}")