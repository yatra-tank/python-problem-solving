# Given k, examine all subarrays of size k and return maximum sum.
L = eval(input("Enter a list of numbers: "))
k = int(input("Enter a number: "))

s = 0
for i in range(k):
    s = s + L[i]

m = s

# Slide the window through the rest of the list
for i in range(k, len(L)):
    s = s + L[i] - L[i - k]
    if s > m:
        m = s

print(m)