"""
CodeAlpha Python Internship - Task 1: Hangman Game
A simple text-based Hangman game.

Concepts used: random, while loop, if-else, strings, lists.
"""

import random

WORDS = ["python", "hangman", "developer", "internship", "keyboard"]
MAX_WRONG_GUESSES = 6

# ASCII art for each stage (0 wrong guesses ... 6 wrong guesses)
HANGMAN_STAGES = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========""",
]


def display_word(word, guessed_letters):
    """Return the word with unguessed letters shown as underscores."""
    shown = []
    for letter in word:
        if letter in guessed_letters:
            shown.append(letter)
        else:
            shown.append("_")
    return " ".join(shown)


def get_guess(guessed_letters):
    """Keep asking until the player enters a valid, new single letter."""
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
        else:
            return guess


def play_game():
    """Play one round of Hangman."""
    word = random.choice(WORDS)
    guessed_letters = []
    wrong_guesses = 0

    print("\n=== HANGMAN ===")
    print(f"The word has {len(word)} letters. You can miss {MAX_WRONG_GUESSES} times.")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print(HANGMAN_STAGES[wrong_guesses])
        print("\nWord:", display_word(word, guessed_letters))
        print("Guessed letters:", ", ".join(sorted(guessed_letters)) or "none")
        print(f"Wrong guesses left: {MAX_WRONG_GUESSES - wrong_guesses}")

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

        # Check for a win: every letter of the word has been guessed
        if all(letter in guessed_letters for letter in word):
            print("\nWord:", display_word(word, guessed_letters))
            print(f"Congratulations, you won! The word was '{word}'.")
            return

    # Loop ended because the player ran out of guesses
    print(HANGMAN_STAGES[MAX_WRONG_GUESSES])
    print(f"\nGame over! The word was '{word}'.")


def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
