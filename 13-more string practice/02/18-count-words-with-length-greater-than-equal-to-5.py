# Given a sentence, count how many words have length at least 5.
def function(s):
    word = s.split()
    count = 0

    for i in word:
        length = len(i)
        if length >= 5:
            count += 1

    return count

s = input("Enter a string: ")
print(function(s))