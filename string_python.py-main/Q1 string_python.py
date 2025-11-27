text = input("Enter a string: ")

text_lower = text.lower()

if text_lower == text_lower[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
