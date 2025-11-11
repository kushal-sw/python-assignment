# A 3 digit integer number (randomly genrated) the user has to guess the number.
# After each guess, the program provides feedback on how many digits are correct and in the correct position,
# and how many digits are correct but in the wrong position. The game continues until 10 attempts.
 import random

 three_digit_number = random.randrange(100, 999) # Example number, in a real game this would be randomly generated
 attempts = 10

 while attempts > 0 and attempts <= 10:
     guess = input("Enter your 3-digit guess: ")

     if len(guess) != 3 is not str(guess).isdigit():
         attempts = attempts - 1
         print(f"Enter a valid 3-digit number. you entered {len(guess)} digits.")

         if str(guess) == three_digit_number:
             print("Congratulations! You've guessed the number correctly.")
             break

     else:
          print(f"Incorrect guess. Try again you have {attempts} attempts left.")
          for x in list(guess):
              if x in str(three_digit_number):
                  if str(three_digit_number).index(x) == guess.index(x):
                      print(f"Digit {x} is in the correct position.")
                  if str(three_digit_number).index(x) != guess.index(x):
                         print(f"Digit {x} is in the wrong position.")

#Question : Birthday Paradox
#Code
import random
def simulate_birthday_paradox(num_people, simulations=100):
"""Simulate the Birthday Paradox to calculate the probability."""
match_count = 0
for
_
duplicates
in range(simulations):
birthdays = [random.randint(1, 365) for
_
in range(num_people)]
if len(birthdays) != len(set(birthdays)): # Check for
match_count += 1
probability = match_count / simulations
return probability
if __name__ == "__main__":
print("Birthday Paradox Simulation")
num_people = int(input("Enter the number of people in the group: "))
probability = simulate_birthday_paradox(num_people)
print(f"The probability of at least two people sharing a birthday in
a group of {num_people} is approximately {probability:.2%}.")
#Output
Birthday Paradox Simulation
Enter the number of people in the group: 23
The probability of at least two people sharing a birthday in a group of
23 is approximately 49.50%.
