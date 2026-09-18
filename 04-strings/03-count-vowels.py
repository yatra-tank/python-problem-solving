# Count vowels (a, e, i, o, u – you can decide if you treat uppercase as vowel too).
s = input("Enter a string: ").lower()
count = 0
for i in s:
    if i in 'aeiou':
        count += 1
print(count)