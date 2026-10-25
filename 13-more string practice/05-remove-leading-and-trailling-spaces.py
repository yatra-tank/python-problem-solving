# Return a new string with spaces removed from start and end only.
def function(s):
    s1 = ""

    for i in s:
        if i == " ":
            continue
        else:
            s1 += i

    return s1

s = input("Enter a string: ")
print(function(s))