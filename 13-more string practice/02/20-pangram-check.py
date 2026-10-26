# A pangram contains every letter a–z at least once (ignore case and non-letters).
def function(s):
    for i in range(26):
        found = False
        for j in s:
            if chr(65 + i) == j:
                found = True
                break
        if not found:
            return "false"
    return "true"

s = input("Enter a string: ").strip().upper()
print(function(s))