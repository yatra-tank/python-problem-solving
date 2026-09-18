# Given a string, remove all digits.
s = input("Enter a string: ")
result = ""
for i in s:
    if i not in '0123456789':
        result += i
print(result)