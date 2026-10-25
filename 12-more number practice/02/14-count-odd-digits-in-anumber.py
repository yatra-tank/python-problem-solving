# Given a number, count how many digits are odd.
def function(n):
    odd = 0

    for i in n:
        if int(i)%2 != 0:
            odd += 1
    print(odd)

n = input("Enter a number: ")
function(n)