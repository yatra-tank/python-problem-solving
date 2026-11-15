# Given string, compress consecutive duplicates into a single occurrence.
s = input("Enter a string: ")
empty_s = ""

for i in s:
    if len(empty_s) == 0 or i != empty_s[-1]:
        empty_s += i

print(empty_s)