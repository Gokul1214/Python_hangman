# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import validation as v
print("Welcome to a game of Hangman. Objective of the game is to guess the name of the movie.")
print("You start guessing letters that may be a part of the movie. After 5 incorrect guesses the you lose the game.")
print("Enjoy playing!!!!!")

def main():

    word = "Zootopia"
    word = word.lower()
    #output list
    guess_word = ''
    guess_word += v.letter_check(guess_word, word)

    if guess_word == word:
        print("Congratulations on solving this Hangman puzzle!!!!!")
    else:
        print("You were unfortunately not able to solve the Hangman puzzle. The name of the movies was ", word)
main()
