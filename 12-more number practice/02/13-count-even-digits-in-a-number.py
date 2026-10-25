# Given a number, count how many digits are even.
def function(n):
    even = 0

    for i in n:
        if int(i)%2 == 0:
            even += 1
    print(even)

n = input("Enter a number: ")
function(n)