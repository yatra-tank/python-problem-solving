# Students as array of objects: {name, marks}.
d = {}
n = int(input("Enter number of entries: "))

for i in range(n):
    name = input("Enter your name: ")
    marks = int(input("Enter your marks: "))

    d[name] = marks

highest = max(d.values())

for i in d:
    if d[i] == highest:
        print(i)
        break