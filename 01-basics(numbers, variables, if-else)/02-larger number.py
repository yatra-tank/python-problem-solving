# Given two numbers, print the larger one.
a, b= map(int, input("Enter two numbers separated by space: ").split()[:2])
if a>b:
    print(a)
else:
    print(b)
