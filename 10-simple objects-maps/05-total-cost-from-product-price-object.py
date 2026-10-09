# Given object of {productName : price}, find total.
d = {}
n = int(input("Enter number of entries: "))

for i in range(n):
    pname = input("Enter product name: ")
    price = int(input("Enter price: "))

    d[pname] = price

total = 0

for i in d:
    total += d[i]

print(d)
print("Total =", total)