import random
print("WELCOME TO THE NUMBER GUESSING GAME")
lower_bound =int(input("Enter the lower_bound:"))
upper_bound =int(input("Enter the upper_bound:"))
secret_number = random.randint(lower_bound, upper_bound)
Attempts=0
while True:# loop executes until the  condition is true or satified
    try:
        guess_the_number = int(input("Guess the number:"))
        if lower_bound > guess_the_number or upper_bound < guess_the_number:#checks whether the entered number in range
            print("you entered a out of range number!.\nplease enter a valid number!")
            Attempts += 1
        elif secret_number > guess_the_number:  # guess_the_number < secret_number
            print("Too low! Try again.")
            Attempts += 1
        elif secret_number < guess_the_number:
            print("Too high! Try again.")
            Attempts += 1
        else:
            Attempts += 1
            print("Congratulations!You guessed it!", guess_the_number)
            print("the no.of attempts are", Attempts)#the no.of will be printed here
            break

    except ValueError:
        print("ValueError. Please enter a valid number.")
        break
