# Given a string, remove vowels (a, e, i, o, u – you can treat uppercase similarly).
s = input("Enter a string: ")
result = ""
for i in s:
    if i not in 'aeiouAEIOU':
        result += i
print(result)