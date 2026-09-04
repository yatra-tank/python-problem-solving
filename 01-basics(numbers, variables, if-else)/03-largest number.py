# Given three numbers, print the largest.
a, b, c= map(int, input("Enter three numbers separated by space: ").split()[:3])
print(max(a, b, c))

# OR 

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)
