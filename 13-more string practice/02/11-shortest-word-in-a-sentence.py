# Return the actual word with minimum length (if tie, you can return first shortest).
def function(s):
    L = []
    word = s.split()

    for i in word:
        L.append(len(i))

    return min(L)

s = input("Enter a string: ")
print(function(s))