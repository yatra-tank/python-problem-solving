# Return the middle charcter for odd length, middle two characters for even length.
def function(s):
    length = len(s)
    if length % 2 != 0:
        mid = length // 2
        return s[mid]
    else:
        chr1 = length // 2 - 1
        chr2 = length // 2
        return s[chr1] + s[chr2]

s = input("Enter a string: ")
print(function(s))