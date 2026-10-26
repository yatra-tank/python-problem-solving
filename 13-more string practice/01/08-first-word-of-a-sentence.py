# Characters from start until first space. If no spcae, whole string.
def function(s):
    empty_s = ""

    for i in s:
        if i == " ":
            break
        empty_s += i

    return empty_s

s = input("Enter a string: ")
print(function(s))