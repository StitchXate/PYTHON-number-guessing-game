import random

number = random.randint(1, 100)

guess = 0
attempts = 0

print("=== Number Guessing Game ===")
print("Guess a number between 1 and 100")

while guess != number:

    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low")

    elif guess > number:
        print("Too high")

    else:
        print("Congratulations! You guessed the number.")
        print("Total attempts:", attempts)
