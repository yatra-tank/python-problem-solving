# Given a string, count uppercase letters.
s = input("Enter a string: ")
count = 0
for i in s:
    if i.isupper() == True:
        count += 1
print(count)