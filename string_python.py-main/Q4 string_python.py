text = input("Enter a string: ")

vowels = digits = spaces = consonants = 0

for char in text:
    if char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    elif char.isalpha():
        if char.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)