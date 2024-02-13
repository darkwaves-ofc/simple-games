import random
from login import LoginController


class HangMan:

    @staticmethod
    def choose_word():
        word_list = ["apple", "banana", "orange",
                     "strawberry", "grape", "watermelon", "pineapple"]
        # Choose a random word from the list
        return random.choice(word_list)

    @staticmethod
    def display_word(word, guessed_letters):
        # Display the word with guessed letters revealed and unguessed letters hidden
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display

    @staticmethod
    def hangman(username, game):
        controller = LoginController()
        print("Welcome to Hangman!")
        word = HangMan.choose_word()
        guessed_letters = []
        max_attempts = 6
        attempts = 0

        while attempts < max_attempts:
            print("\n" + HangMan.display_word(word, guessed_letters))
            guess = input("Guess a letter: ").lower()

            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
                continue
            elif len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
                continue

            guessed_letters.append(guess)

            if guess not in word:
                attempts += 1
                print("Incorrect guess. You have",
                      max_attempts - attempts, "guesses left.")
            else:
                print("Good guess!")

            if all(letter in guessed_letters for letter in word):
                print("\nCongratulations! You guessed the word:", word)
                controller.save_user_score(username, game["score"])
                break

        if attempts == max_attempts:
            print("\nSorry, you ran out of guesses. The word was:", word)
