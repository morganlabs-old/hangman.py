#!/bin/env python
MAX_LIVES = 10


class Game:
    word = []
    correct_guesses = []
    letters_guessed = []
    lives_used = 0

    def __init__(self):
        self.word = list("somethsings")
        self.correct_guesses = [""] * len(self.word)

    def get_guess(self):
        guess = input("What's your guess? ")
        if len(guess) != 1:
            self.handle_word_guess(guess)
        else:
            self.handle_letter_guess(guess)

    def handle_letter_guess(self, guess):
        if guess in self.letters_guessed:
            print("That has already been guessed!")
            self.get_guess()
            return

        if not guess.isalpha():
            print("Please only enter letters!")
            self.get_guess()
            return
        self.letters_guessed.append(guess.lower())

        for i in range(len(self.word)):
            if (self.word[i] == guess):
                self.correct_guesses[i] = guess

    def handle_word_guess(self, guess):
        print("Placeholder")

    def use_life(self):
        self.lives_used += 1
        if self.lives_used >= MAX_LIVES:
            self.lives_used = MAX_LIVES
            self.game_over()

    def game_over(self):
        print("Placeholder")


game = Game()
print(game.word)
print(game.correct_guesses)
game.get_guess()
print(game.correct_guesses)
