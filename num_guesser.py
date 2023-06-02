# This is a module
import random

# # Range does not include the typed param numbers
# rng = random.randrange(-3, 12)
#
# # Int DOES include the typed param numbers
# nt = random.randint(1, 10)

# This will always return a string regardless of if it is a number
user_input = input("Enter in a max range number: ")

# this checks if the string contains a digit(numeric value) or not
if user_input.isdigit():
    # This converts the string into a numeric form
    user_input = int(user_input)

    if user_input < 0:
        print("Invalid Entry. Enter a number greater than 0!")
        quit()
else:
    print("Invalid Entry. Please enter a number!")
    quit()

random_guess = random.randrange(0, user_input)

while True:
    user_guess = input("Now, guess the randomized number: ")

    if user_guess.isdigit():
        # This converts the string into a numeric form
        user_guess = int(user_guess)
    else:
        print("Enter a number: ")

        # brings us back to the top of the while loop
        continue

    if user_guess == random_guess:
        print("CORRECT")
        quit()
    else:
        # I could also just make this an elif
        if user_guess > random_guess:
            print("Your guess is greater than the random number!")
        else:
            print("Your guess is less than the random number!")