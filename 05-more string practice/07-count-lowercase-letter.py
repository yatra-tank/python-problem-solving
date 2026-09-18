# Given a string, count lowercase letters.
s = input("Enter a string: ")
count = 0
for i in s:
    if i.islower() == True:
        count += 1
print(count)