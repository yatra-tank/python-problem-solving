# Given an array of strings, count how many have length greater than 3.
L = eval(input("Enter a list of strings: "))
length = []
count = 0

for i in L:
    word_len = 0

    for j in range(len(i)):
        word_len += 1   
    length.append(word_len)

for i in length:
    if i > 3:
        count += 1

print(count)