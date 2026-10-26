# Return new string with every ? replaced by !.
def function(s):
    empty_s = ""
    for i in s:
        if i == "?":
            empty_s += "!"
        else:
            empty_s += i
            
    return empty_s

s = input("Enter a string: ")
print(function(s))