#!/bin/env python
MAX_LIVES = 10


class Game:
    lives_used = 0
    letters_guessed = []

    # Recieves an input from stdin
    # Checks if it has already been guessed. If so, allow the user to retry
    # If not, add it to self.letters_guessed
    def get_guess(self):
        guess = input("What's your guess? ")
        if guess in self.letters_guessed:
            print("That has already been guessed!")
            self.get_guess()
            return
        self.letters_guessed.append(guess)


game = Game()
game.get_guess()
print(game.letters_guessed)
game.get_guess()
game.get_guess()
print(game.letters_guessed)
