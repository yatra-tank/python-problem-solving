# Print first N multiples of 7.
n = int(input("Enter a number: "))
product = 1
for i in range(1, n + 1):
    product = i *7
    print(product, end=" ")