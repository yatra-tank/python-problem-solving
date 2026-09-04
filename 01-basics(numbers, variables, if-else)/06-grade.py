# Given marks 0–100, print grade.
marks = int(input("Enter your marks: "))
if 90<marks<100:
    print("A")
elif 80<marks<89:
    print("B")
elif 70<marks<79:
    print("C")
elif 60<marks<69:
    print("D")
elif 0<marks<59:
    print("F")
else:
    print("Please enter valid marks")
 