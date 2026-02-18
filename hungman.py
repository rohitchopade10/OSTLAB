# Hangman game - Python 3
# Paste into OnlineGDB or run locally with `python hangman.py`

import random
import sys

HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

WORD_LIST = [
    "python", "hangman", "computer", "program", "network", "developer",
    "function", "variable", "algorithm", "database", "internet", "github"
]

def choose_word():
    return random.choice(WORD_LIST).lower()

def display_state(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()
    print("Missed:", " ".join(sorted(missed_letters)) or "None")
    # show the secret word with underscores for missing letters
    displayed = [ch if ch in correct_letters else "_" for ch in secret_word]
    print("Word: ", " ".join(displayed))
    print()

def get_guess(already_guessed):
    while True:
        guess = input("Guess a letter (or full word): ").strip().lower()
        if not guess:
            print("Please enter a letter or a word.")
            continue
        if len(guess) == 1:
            if not guess.isalpha():
                print("Enter a letter (a-z).")
            elif guess in already_guessed:
                print("You already guessed that letter. Try again.")
            else:
                return guess
        else:
            # user guessed a full word
            if not guess.isalpha():
                print("Word must contain letters only.")
            else:
                return guess

def play_again():
    return input("Play again? (y/n): ").strip().lower().startswith("y")

def play_hangman():
    print("Welcome to Hangman!")
    secret_word = choose_word()
    missed_letters = set()
    correct_letters = set()
    game_over = False

    while True:
        display_state(missed_letters, correct_letters, secret_word)

        guess = get_guess(missed_letters.union(correct_letters))

        # full-word guess
        if len(guess) > 1:
            if guess == secret_word:
                print("\nAmazing! You guessed the word:", secret_word)
                game_over = True
            else:
                print("\nThat's not the word.")
                missed_letters.add(guess)  # count a wrong word-guess as a miss
        else:
            # single letter guess
            if guess in secret_word:
                correct_letters.add(guess)
                # check if all letters found
                if all(ch in correct_letters for ch in secret_word):
                    print("\nCongratulations! You guessed the word:", secret_word)
                    game_over = True
            else:
                missed_letters.add(guess)
                # lose condition: too many misses
                if len(missed_letters) >= len(HANGMAN_PICS) - 1:
                    display_state(missed_letters, correct_letters, secret_word)
                    print("You ran out of guesses! The word was:", secret_word)
                    game_over = True

        if game_over:
            if play_again():
                secret_word = choose_word()
                missed_letters.clear()
                correct_letters.clear()
                game_over = False
                print("\nStarting a new game...\n")
            else:
                print("Thanks for playing. Goodbye!")
                break

if __name__ == "__main__":
    try:
        play_hangman()
    except KeyboardInterrupt:
        print("\nGame interrupted. Bye!")
        sys.exit(0)
