import random

number = random.randint(1,25)
number_of_guess = 0

while number_of_guess <5:
    print("Guess a number between 1 to 25: ")
    guess = input()
    guess = int(guess)
    number_of_guess += 1

    if guess == number:
        break
    elif number_of_guess ==5:
        break
    else:
        print("Nope! Try again")
if guess == number:
    print("Correct! you guess number in " + str(number_of_guess) + "tries")
else:
    print("You did not guess the number. The number is: " + str(number) + ".")