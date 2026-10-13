# Two numbers are co-prime if their GCD is 1.
def composite(a, b):
    if a < b:
        small = a
    else:
        small = b

    for i in range(1, small + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    if gcd == 1:
        print("true")
    else:
        print("false")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
composite(a, b)