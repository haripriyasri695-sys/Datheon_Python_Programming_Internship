
import random

words = ["apple", "mango", "tiger", "banana", "python"]
secret_word = random.choice(words)

guessed_letters = set()
wrong_guesses = set()
max_attempts = 6

stages = [
    """
     -----
     |   |
         |
         |
         |
    =========
""",
    """
     -----
     |   |
     O   |
         |
         |
    =========
""",
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
""",
    """
     -----
     |   |
     O   |
    /|   |
         |
    =========
""",
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
""",
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
""",
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
"""
]

print("Welcome to Hangman!")

while len(wrong_guesses) < max_attempts:
    print(stages[len(wrong_guesses)])

    display_word = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )

    print("Word:", display_word)
    print("Wrong guesses:", len(wrong_guesses))
    print("Attempts left:", max_attempts - len(wrong_guesses))

    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You won!")
        break

    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter!")
        continue

    if guess in guessed_letters or guess in wrong_guesses:
        print("You already guessed that letter!")
        continue

    if guess in secret_word:
        guessed_letters.add(guess)
        print("Correct guess!")
    else:
        wrong_guesses.add(guess)
        print("Wrong guess!")

else:
    print(stages[max_attempts])
    print("\nGame over!")
    print("The word was:", secret_word)

print("Thanks for playing!")
