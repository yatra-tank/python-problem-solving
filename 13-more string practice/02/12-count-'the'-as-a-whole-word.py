# Count how many times 'the' appears as a separate word (case-insensitive if you like).
def function(s):
    count = 0

    for i in s.split():
        if i == "the":
            count += 1

    return count

s = input("Enter a string: ")
print(function(s))