import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("------------------------------------------------")
    print("Welcome to the Number Guessing game!")
    print("------------------------------------------------")
    print("The number is between 1 and 100.")
    print('\t')

    while True:
        user_input = input("Take a guess: ")

        # Check if the input is a valid integer
        if user_input.isdigit():
            user_guess = int(user_input)
            attempts += 1

            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                break
        else:
            print("Invalid input. Please enter a valid number between 1 and 100.")

if __name__ == "__main__":
    guess_the_number()
