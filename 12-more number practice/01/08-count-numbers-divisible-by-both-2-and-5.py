# Effectively numbers divisible by 10.
def function(n):
    count = 0
    for i in range(1, n + 1):
        if i%2 == 0 and i%5 == 0:
            count += 1
    print(count)

n = int(input("Enter a number: "))
function(n)