# Count consonants (letters that are not vowels).s = input("Enter a string: ").lower()
s = input("Enter a string: ").lower().replace(" ", "")
count = 0
for i in s:
    if i not in 'aeiou':
        count += 1
print(count)