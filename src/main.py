#!/bin/env python
MAX_LIVES = 10


class Game:
    lives_used = 0
    letters_guessed = []

    def get_guess(self):
        guess = input("What's your guess? ")
        if guess in self.letters_guessed:
            print("That has already been guessed!")
            self.get_guess()
            return

        if not guess.isalpha():
            print("Please only enter letters!")
            self.get_guess()
            return
        self.letters_guessed.append(guess)

    def use_life(self):
        self.lives_used += 1
        if self.lives_used >= MAX_LIVES:
            self.lives_used = MAX_LIVES
            self.game_over()

    def game_over(self):
        print("Placeholder")


game = Game()
