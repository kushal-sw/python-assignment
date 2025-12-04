#this file is for problems in python this is problem 1
#there will be 3 digit nummber (integer) user se input lenge agar 3 digit nahi hai to error message dena hai

# number = 245
# if len(str(number)) != 3:
    # print("you guessed it right 😎")
# num = input("Please enter a 3-digit integer: ")
# if len(num) != 3 or not num.isdigit():
    # print("Error: Input must be a 3-digit integer.")



#number = 245
#if len(str(number)) != 3:
 #   print("you guessed it right 😎")








three_digit_number = 245
tries = 10
while tries > 0:
    user_input = int(input("enter a random guess for the number:"))

    tries = tries - 1 
    if user_input == three_digit_number:
        print("you guessed it right 😎")
        break
    
    else:
        print(f"try again you have {tries} left")
        if user_input > three_digit_number:
            print ("you have guessed higher number than the actual number")
        else:
            print ("you have guessed lower number than the actual number")

        correct_digits = 0
        for x in range(3):
            if str(user_input)[x] == str(three_digit_number)[x]:
                correct_digits += 1
        print(f"You got {correct_digits} digit(s) correct in the right position.")
