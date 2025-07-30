import random

# List of words
words = ["python", "internship", "shadowfox", "programming", "hangman", "code", "meghana"]

def choose_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = 6

    print(" Welcome to Hangman!")
    print("_ " * len(word))

    while incorrect_guesses < max_attempts:
        guess = input("\nEnter a letter: ").lower()

        # Validate input
        if not guess.isalpha() or len(guess) != 1:
            print(" Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print(" You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(" Good guess!")
        else:
            incorrect_guesses += 1
            print(f" Wrong guess! Attempts left: {max_attempts - incorrect_guesses}")

        current_display = display_word(word, guessed_letters)
        print("\nWord: ", current_display)

        if "_" not in current_display:
            print("\n Congratulations! You guessed the word:", word)
            break
    else:
        print("\n Game Over! The word was:", word)

# Play again loop
while True:
    hangman()
    again = input("\n Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print(" Thanks for playing Hangman!")
        break