import random

lowest_number = 1
highest_number = 100
answer = random.randint(lowest_number, highest_number)

print("Welcome to Martin's Guessing Game!")
print("Choose difficulty:")
print("1. Easy - 10 guesses")
print("2. Medium - 7 guesses")
print("3. Hard - 5 guesses")

difficulty = input("Choose 1, 2, or 3: ")

if difficulty == "1":
    max_guesses = 10
elif difficulty == "2":
    max_guesses = 7
elif difficulty == "3":
    max_guesses = 5
else:
    print("Invalid choice. Easy selected.")
    max_guesses = 10

guesses = 0

print(f"Guess a number between {lowest_number} and {highest_number}")

while guesses < max_guesses:

    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Invalid guess")
        continue

    guess = int(guess)

    if guess < lowest_number or guess > highest_number:
        print("Number is out of range")
        continue

    guesses += 1
    remaining = max_guesses - guesses

    if guess < answer:
        print("Too low!")

    elif guess > answer:
        print("Too high!")

    else:
        print(f"Correct! The answer was {answer}")
        print(f"You used {guesses} guesses")
        break

    print(f"Remaining guesses: {remaining}")

else:
    print("Game over!")
    print(f"The answer was {answer}")