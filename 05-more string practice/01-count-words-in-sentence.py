# Given a sentence, count how many words it has (split by spaces, ignore extra spaces if you want).
s = input("Enter a string: ").strip()
count = 0
for i in s.split():
    count += 1
print(count)