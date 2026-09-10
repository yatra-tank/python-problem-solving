n = int(input("Enter a number: "))
rev = 0
flag = False

if n < 0:
    flag = True
    n = -n

while n != 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
    
if flag:
    print(-rev)
else:
    print(rev)