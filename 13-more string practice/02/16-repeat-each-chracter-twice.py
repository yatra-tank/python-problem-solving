# New string where each char appears twice.
def function(s):
    for i in s:
        print(i + i, end= "")

s = input("Enter a string: ")
function(s)