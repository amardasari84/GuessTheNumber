Problem Statement- 


•	Build a number Guessing Game in which the user selects a range. 
•	 Assume the user selected a range from X to Y where both X and Y are   integers.
•	So a random number in that range is selected by the system where the user needs to guess the minimum number of guesses.


Algorithm-
	Initialise the Game
•	Print a welcome message.
	Get Range from User
•	 Prompt the user to enter the lower bound .
•	 Prompt the user to enter the upper bound.
•	 Validate that lower_boundis less than or equal to upper_bound
•	 If validation fails, prompt the user again.
	Select Random Number
•	Generate a random number within the range [lower_bound,upper_bound].
	Initialize Guess Counter
•	Set the guess counter to 0.
	Start Guessing Loop
	Repeat until the user guesses the correct number:
•	Prompt the user to enter a guess.
•	Increment the guess counter.
•	Validate that the guess is within the range [lower_bound, upper_bound].
	If not, prompt the user again.
	Compare the guess to the secret number:
	If the guess is less than the secret number, inform the user that the guess is too low.
	If the guess is greater than the secret number, inform the user that the guess is too high.
	If the guess is equal to the secret number, inform the user that they have guessed correctly and display the number of attempts.
  End Game.
•	Print a congratulatory message along with the number of attempts taken.
 



Pseudo code-

START
    PRINT "Welcome to the Number Guessing Game!"

    DO
        PRINT "Enter the lower bound X: "
        READ lower_bound
        PRINT "Enter the upper bound Y: "
        READ upper_bound
        IF lower_bound > upper_boundTHEN
            PRINT "Invalid range. Lower bound must be less than or equal to upper      bound."
        END IF
    WHILE lower_bound> upper_bound

    SET secret_number TO RANDOM(lower_bound, upper_bound)
    SET attempts TO 0

    PRINT "Guess the number between lower_bound and upper_bound!"

    DO
        PRINT "Enter your guess: "
        READ guess
        INCREMENT attempts BY 1

        IF guess < lower_bound OR guess > upper_bound THEN
            PRINT "Please guess a number within the range lower_bound to upper_bound."
        ELSE IF guess_the_number < secret_number THEN
            PRINT "Too low! Try again."
        ELSE IF guess_the_number > secret_number THEN
            PRINT "Too high! Try again."
        ELSE
            PRINT "Congratulations! You guessed the number secret_number in attempts."
        END IF
    WHILE guess != secret_number

END

