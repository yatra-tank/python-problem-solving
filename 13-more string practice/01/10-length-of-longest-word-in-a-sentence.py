# Return just the number (length of the longest word).
def function(s):
    L = []
    word = s.split()

    for i in word:
        L.append(len(i))

    return max(L)

s = input("Enter a string: ")
print(function(s))