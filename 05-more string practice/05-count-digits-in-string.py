# Given a string, count how many characters are digits (0–9).
s = input("Enter a string: ")
count = 0
for i in s:
    if i in '0123456789':
        count += 1
print(count)