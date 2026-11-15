# Return first character that appears exactly once, or null if none.
s = input("Enter a string: ")

found = False

for i in s:
    count = 0
    for j in s:
        if i == j:
            count += 1

    if count == 1:
        print(i)
        found = True
        break

if not found:
    print("null")