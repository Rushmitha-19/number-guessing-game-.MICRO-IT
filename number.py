import random

def number_guessing_game():
    """
    Implements a simple number guessing game.
    The player tries to guess a randomly generated number within a specified range.
    """
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess it.")

    # 1. Generate a random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            # 2. Get player input
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))

            # Input validation: ensure the guess is within the valid range
            if not 1 <= guess <= 100:
                print("Please guess a number between 1 and 100.")
                continue # Skip the rest of this loop iteration and ask for input again

            attempts += 1

            # 3. Provide feedback
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                # 4. If the guess is correct
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                break # Exit the loop, as the game is won
        except ValueError:
            print("Invalid input. Please enter a whole number.")
    else:
        # This 'else' block executes if the while loop completes without a 'break'
        # meaning the player ran out of attempts.
        print(f"\nSorry, you ran out of attempts! The secret number was {secret_number}.")

    # 7. Offer to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        number_guessing_game() # Recursively call the game function to play again
    else:
        print("Thanks for playing! Goodbye!")

# Start the game
if __name__ == "__main__":
    number_guessing_game()