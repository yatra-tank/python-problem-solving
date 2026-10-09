# Write a function that returns "positive", "negative", or "zero".
def function(n):
    if n > 0:
        return "postive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

n = int(input("Enter a number: "))
print(function(n))