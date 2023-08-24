import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.")

    while attempts < max_attempts:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low!")
            print_hint(secret_number, guess, "higher")
        elif guess > secret_number:
            print("Too high!")
            print_hint(secret_number, guess, "lower")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

    if attempts == max_attempts:
        print(f"Sorry, you've reached the maximum number of attempts. The number was {secret_number}.")

def print_hint(secret_number, guess, hint):
    if abs(secret_number - guess) <= 10:
        print(f"The secret number is {hint} and close to your guess.")
    else:
        print(f"The secret number is {hint} than your guess.")

if __name__ == "__main__":
    guess_number()
