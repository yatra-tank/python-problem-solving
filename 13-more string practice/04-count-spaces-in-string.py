# Count how many space characters ' ' are present.
def function(s):
    count = 0

    for i in s:
        if i == " ":
            count += 1

    return count

s = input("Enter a string: ")
print(function(s))