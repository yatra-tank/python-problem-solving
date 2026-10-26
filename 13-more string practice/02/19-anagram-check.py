# Two strings are anagrams if they use same letters in same counts, order doesn’t matter.
def function(s1, s2):
    count = 0

    if len(s1) == len(s2):
        for i in s1:
            for j in range(len(s1)):
                if i in s2[j]:
                    count += 1
    else:
        return "false"

    if len(s1) == count:
        return "true"
    else:
        return "false"

s1 = input("Enter a string: ").strip().lower()
s2 = input("Enter another string: ").strip().lower()
print(function(s1, s2))