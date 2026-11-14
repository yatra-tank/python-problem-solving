# Check if there exist three numbers whose sum equals target.
L = eval(input("Enter a list of numbers: "))
target = int(input("Enter a number: "))

found = False
for i in range(len(L)):
    for j in range(i + 1, len(L)):
        for k in range(j + 1, len(L)):
            if L[i] + L[j] + L[k] == target:
                found = True
                break
        if found:
            break
    if found:
        break

if found:
    print("true")
else:
    print("false")
