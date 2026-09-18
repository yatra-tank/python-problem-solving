# Check if a string is a palindrome.
s = input("Enter a string: ")
if s == s[::-1]:
    print("is a palindrome")
else:
    print("not a palindrome")