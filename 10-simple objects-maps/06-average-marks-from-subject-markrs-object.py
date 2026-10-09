# Object like {math: 80, science: 90, english: 70}
d = {}
n = int(input("Enter number of entries: "))

for i in range(n):
    sub = input("Enter subject name: ")
    marks = int(input("Enter marks: "))

    d[sub] = marks

total = 0

for i in d:
    total += d[i]

print(d)

if n == 0:
    print("Average: 0")
else:
    print("Average:", total / n)