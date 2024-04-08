#!/bin/env python
import json
import os
import random

MAX_LIVES = 8
DIFFICULTIES = ["easy", "normal", "hard"]


class Game:
    word = []
    correct_guesses = []
    letters_guessed = []
    lives_used = 0
    difficulty = ""

    def start(self):
        self.get_difficulty()

        self.get_word()
        self.correct_guesses = [""] * len(self.word["word"])

        self.game_loop()

    def game_loop(self):
        print("Welcome to Hangman!")
        print("The idea is simple. I'll think of a word, and you can guess letters or words to figure it out!")
        print("Be careful, however! For each wrong answer, this little stickman will come closer and closer to death! :(")
        self.print_ui()
        self.get_guess()

        is_game_over = self.is_game_over()
        if is_game_over:
            self.print_ui()
            self.game_over()
            return

        is_word_guessed = self.is_word_guessed()
        if is_word_guessed:
            self.game_complete()
            return

        self.game_loop()

    def get_difficulty(self):
        difficulties = ", ".join(DIFFICULTIES)
        print(f"Available difficulties: {difficulties}")
        difficulty = input("What difficulty would you like to use? ")
        difficulty = difficulty.lower()

        if difficulty not in DIFFICULTIES:
            print("That difficulty does not exist!")
            self.get_difficulty()
            return

        self.difficulty = difficulty

    def get_word(self):
        with open(os.path.dirname(os.path.abspath(__file__))
                  + "/words.json") as words_raw:
            words = json.load(words_raw)

        self.word = random.sample(words[self.difficulty], 1)[0]

    def print_ui(self):
        self.clear_screen()
        self.print_correct_guesses()
        self.print_hangman()
        self.print_incorrect_guesses()

    def print_correct_guesses(self):
        correct_guesses_str = map(
            lambda x: x if x != "" else "_", self.correct_guesses
        )
        correct_guesses_str = "".join(correct_guesses_str)

        print(correct_guesses_str)

    def print_incorrect_guesses(self):
        incorrect_guesses_str = filter(
            lambda x: False if x in self.correct_guesses else True,
            self.letters_guessed
        )
        incorrect_guesses_str = " ".join(incorrect_guesses_str)

        print(incorrect_guesses_str)

    def print_hangman(self):
        hangman = [""] * 8

        # See, I know there's like a 99.99999% chance there's an easier way to
        # do this... but idk it so :shrug:
        if self.lives_used >= 0:
            hangman[0] = ""
            hangman[1] = ""
            hangman[2] = ""
            hangman[3] = ""
            hangman[4] = ""
            hangman[5] = ""
            hangman[6] = ""
            hangman[7] = "_____"
        if self.lives_used >= 1:
            hangman[0] = ""
            hangman[1] = " |"
            hangman[2] = " |"
            hangman[3] = " |"
            hangman[4] = " |"
            hangman[5] = " |"
            hangman[6] = " |"
            hangman[7] = "_|___"
        if self.lives_used >= 2:
            hangman[0] = "  _______"
        if self.lives_used >= 3:
            hangman[1] = " |/      |"
            hangman[2] = " |      (_)"
        if self.lives_used >= 4:
            hangman[3] = " |       |"
            hangman[4] = " |       |"
        if self.lives_used >= 5:
            hangman[3] = " |      \\|"
        if self.lives_used >= 6:
            hangman[3] = " |      \\|/"
        if self.lives_used >= 7:
            hangman[5] = " |      /"
        if self.lives_used >= 8:
            hangman[5] = " |      / \\"

        print("\n".join(hangman))
        print(f"{self.lives_used}/{MAX_LIVES}")

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

        for i in range(len(self.word["word"])):
            if (self.word["word"][i] == guess):
                self.correct_guesses[i] = guess

        if guess not in self.correct_guesses:
            self.use_life()

    def handle_word_guess(self, guess):
        word_str = "".join(self.word["word"]).lower()
        guess = guess.lower()

        if word_str == guess:
            self.correct_guesses = self.word["word"]
        else:
            self.use_life()
            self.use_life()

    def use_life(self):
        self.lives_used += 1

    def is_game_over(self):
        return self.lives_used >= MAX_LIVES

    def is_word_guessed(self):
        return "".join(self.correct_guesses) == "".join(self.word["word"])

    def game_over(self):
        word = "".join(self.word["word"])
        print("Too bad! Better luck next time.")
        print(f"The word was {word}")

    def game_complete(self):
        word = "".join(self.word["word"])
        print("Congratulations! You guessed the word.")
        print(f"The word was {word}")

    def clear_screen(self):
        print("\033[H\033[J", end="")


def main():
    game = Game()
    game.start()


main()
