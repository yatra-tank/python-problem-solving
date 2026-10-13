# Given n, count how many numbers between 1 and n are divisible by 2 or 3.
def function(n):
    count = 0
    for i in range(1, n + 1):
        if i%2 == 0 or i%3 == 0:
            count += 1
    print(count)

n = int(input("Enter a number: "))
function(n)