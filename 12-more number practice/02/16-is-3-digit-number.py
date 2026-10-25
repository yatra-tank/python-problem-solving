# Return true if number is between 100 and 999 (inclusive).
def function(n):
    if 100 <= n <= 999:
        return "true"
    else:
        return "false"

n = int(input("Enter a number: "))
print(function(n))