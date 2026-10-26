# Remove everything that is not a–z, A–Z, or 0–9.
def function(s):
    new_s = ""

    for i in s:
        is_letter = ('a' <= i <= 'z') or ('A' <= i <= 'Z')
        is_digit = ('0' <= i <= '9') 

        if not (is_letter or is_digit):
            continue
        new_s += i

    return new_s

s = input("Enter a string: ")
print(function(s))