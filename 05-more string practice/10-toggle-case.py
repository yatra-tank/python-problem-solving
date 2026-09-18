# Change lowercase to uppercase and uppercase to lowercase.
s = input("Enter a string: ")
result = ""
for i in s:
    i = i.swapcase()
    result += i
print(result)