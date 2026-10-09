# Write a function that returns true if age ≥ 18.
def function(age):
    if age >= 18:
        return True
    else:
        return False

age = int(input("Enter a number: "))
print(function(age))