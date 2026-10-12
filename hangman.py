import random

# List of predefined words
words = ["python", "computer", "programming", "keyboard", "internet"]

# Select a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Set the maximum incorrect guesses
incorrect_guesses = 0
max_attempts = 6

print("=" * 35)
print("       WELCOME TO HANGMAN")
print("=" * 35)

print("Guess the hidden word one letter at a time.")
print("You have 6 incorrect guesses available.")

# Main game loop
while True:

    # Display the current word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_guesses)
    print("Attempts remaining:", max_attempts - incorrect_guesses)

    # Check whether the player has won
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You won!")
        print("The correct word was:", secret_word)
        break

    # Check whether the player has lost
    if incorrect_guesses >= max_attempts:
        print("\nGame over! You lost.")
        print("The correct word was:", secret_word)
        break

    # Ask the player to enter a letter
    guess = input("\nEnter a letter: ").lower().strip()

    # Validate the input
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Please enter one letter.")
        continue

    # Check whether the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    # Save the guessed letter
    guessed_letters.append(guess)

    # Check the guess
    if guess in secret_word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        incorrect_guesses += 1

print("\nThank you for playing Hangman!")