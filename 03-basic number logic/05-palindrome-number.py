# Check if a number reads same forwards and backwards.
n = input("Enter a number: ")
a = int(n[::-1])
n = int(n)
if n == a:
    print("palindrome")
else:
    print("not a palindrome")