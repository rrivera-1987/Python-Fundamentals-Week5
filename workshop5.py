import random

def guess_random_number(tries, start, stop):
    """PLaying a game where we try to guess a randomly chosen number within a range of numbers
    with a limited number of tries."""
    random_number = random.randint(start, stop)

    while tries != 0:
        """Prints the messages to the console that indicate the number of attempts remaining.
        And whether the number guessed is too high or too low."""
        print(f"Number of tries left: {tries}")       
        guess = int(input(f"Guess a number between {start} and {stop}: "))
        if guess == random_number:
            print("Congratulations! You guessed the correct number.")
            return
        elif guess < random_number:
            print("You're way too low!")
        else:
            print("You're way too high!")
        tries -= 1
    print(f"Sorry, you ran out of tries. The number was: {random_number}.")

""" --- Driver test code Task 1 --- 
guess_random_number(5, 0, 10)
tries = 5 """

def guess_random_num_linear(tries, start, stop):
    random_number = random.randint(start, stop)
    print(f"The number for the program to guess is: {random_number}")

    for guess in range(start, stop+1): # The loop itereates over each number in the range between start and stop
        tries -= 1 # The function will iterate through the loop, until there are no more tries left.
        print(f"The program is guessing... {guess}")
        if guess == random_number:
            print("The program has guessed the correct number! :-)")
            return
        if tries == 0:
            break
    print("The program has failed to guess the correct number. :-(")

""" --- Driver test cpde Task 2 --- 
guess_random_num_linear(5, 0, 10)
tries = 5 """

def guess_random_num_binary(tries, start, stop):
    random_number = random.randint(start, stop)
    print(f"Random number to find: {random_number}")
    
    low, high = start, stop # Accessing the possible low and high index.
    while low <= high and tries > 0:
        guess = (low + high) // 2  # Using the floor division operator to guess an integer.
        if guess == random_number:
            print(f"Congratulations, your program found the number: {random_number}")
            return
        elif guess < random_number: # Tells the program that the guess is low and it should guess higher. It also eliminates that guess
            low = guess + 1
            print("Your program is guessing higher")
        else:
            high = guess - 1 # Same as above, but the guess is high so go lower.
            print("Your program is guessing lower")
        tries -= 1
    print("Sorry, your program was not able to guess the number.")

""" --- Driver test code Task 3 --- """
guess_random_num_binary(5, 0, 100)
tries = 5