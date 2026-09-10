# Given two numbers, find their least common multiple.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a > b:
    lcm = a
else:
    lcm = b
    
while True:
    if lcm % a == 0 and lcm % b == 0:
        break  
    lcm += 1
print(lcm) 
