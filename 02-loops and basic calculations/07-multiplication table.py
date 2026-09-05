# Print multiplication table of a given number up to 10.
n = int(input("Enter a number: "))
product = 1
for i in range(1, 11):
    product = i *n
    print(product, end=" ")