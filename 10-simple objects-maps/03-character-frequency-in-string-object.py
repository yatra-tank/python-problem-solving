# Return object of character counts.
s = input("Enter a string: ")
dict = {}

for i in s:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)