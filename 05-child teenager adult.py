# Given an age, print whether the person is "child", "teenager", or "adult" (you can assume: 0–12 child, 13–19 teenager, 20+ adult).
age = int(input("Enter your age: "))
if age <= 12:
    print("child")
elif age <= 19:
    print("teenager")
else:
    print("adult")
