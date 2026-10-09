# Write a function that takes a name and returns "Hello, <name>!".
def greet(s):
    return "Hello, " + s + "!"

s = input("Enter a name: ")
print(greet(s))