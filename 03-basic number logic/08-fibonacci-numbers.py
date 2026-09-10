# Print first N Fibonacci numbers. (Start: 0, 1, 1, 2, 3, …)
n = int(input("Enter a nnumber: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b