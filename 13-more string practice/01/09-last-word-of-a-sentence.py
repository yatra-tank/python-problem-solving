# Characters after the last space. If no space, whole string.
def function(s):
    for i in s.split():
        return s.split()[-1]

s = input("Enter a string: ")
print(function(s))