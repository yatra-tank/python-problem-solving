# Given a number, print whether it is "even" or "odd".
n = int(input("Enter a number: "))
if n%2 == 0:
    print("even")
else:
    print("odd")
    
# Given two numbers, print the larger one.
a, b= map(int, input("Enter two numbers separated by space: ").split()[:2])
if a>b:
    print(a)
else:
    print(b)

# Given three numbers, print the largest.
a, b, c= map(int, input("Enter three numbers separated by space: ").split()[:3])
print(max(a, b, c))
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

# Given a number, print "positive", "negative", or "zero".
n = int(input("Enter a number: "))
if n>0:
    print("positive")
elif n<0:
    print("negative")
else:
    print("zero")

# Given an age, print whether the person is "child", "teenager", or "adult" (you can assume: 0–12 child, 13–19 teenager, 20+ adult).
age = int(input("Enter your age: "))
if age <= 12:
    print("child")
elif age <= 19:
    print("teenager")
else:
    print("adult")

# Given marks 0–100, print grade.
marks = int(input("Enter your marks: "))
if 90<marks<100:
    print("A")
elif 80<marks<89:
    print("B")
elif 70<marks<79:
    print("C")
elif 60<marks<69:
    print("D")
elif 0<marks<59:
    print("F")
else:
    print("Please enter valid marks")
  
# Given a number, print whether it is divisible by 5.
n = int(input("Enter a number: "))
if n%5 == 0:
    print("divisible by 5")
else:
    print("not divisible by 5")

# Given a number, print if it is divisible by both 3 and 5.
n = int(input("Enter a number: "))
if n%3 == 0 and n%5 == 0:
    print("divisible by 3 and 5")
else:
    print("not divisible by 3 and 5")

# Given a year, check if it is a leap year. (Simple version: divisible by 4 → leap; you can refine later.)
n = int(input("Enter year:"))
if n % 4 == 0:
    if n % 100 == 0:
        if n % 400 == 0:
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:
    print("not a leap year")

# Given a number, check if it lies between 10 and 50 (inclusive).
n = int(input("Enter a number: "))
if 10<=n<=50:
    print("in range")
else:
    print("out of range")