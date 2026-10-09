# Write a function that returns true if n is between 1 and 100 (inclusive).
def function(n):
    if 1 <= n <= 100:
        return True
    else:
        return False

n = int(input("Enter a number: "))
print(function(n))