import random

words = ["apple", "banana", "grapes", "orange", "mango"]
word = random.choice(words)

guessed_letters = []
attempts = 6

print("Welcome to Hangman Game!")

while attempts > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("Word:", display_word)

    
    if "_" not in display_word:
        print("You won!")
        break

    guess = input("Guess a letter: ").lower()


    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only ONE letter.")
        continue

    if guess in guessed_letters:
        print(" Already guessed!")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)
    else:
        print("Correct guess!")


if attempts == 0:
    print("You lost! Word was:", word)
