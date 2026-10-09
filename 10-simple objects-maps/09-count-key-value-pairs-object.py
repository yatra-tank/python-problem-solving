# Return how many properties object has.
d = {}
count = 0

n = int(input("Enter number of entries: "))

for i in range(n):
    k = input("Enter your key value: ")
    v = input("Enter your value: ")

    d[k] = v

for i in d:
    count += 1
print(count)