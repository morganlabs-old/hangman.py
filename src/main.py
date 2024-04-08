#!/bin/env python
MAX_LIVES = 10


class Game:
    word = []
    correct_guesses = []
    letters_guessed = []
    lives_used = 0

    def __init__(self):
        self.word = list("laptop")
        self.correct_guesses = [""] * len(self.word)

    def start(self):
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

    def print_ui(self):
        self.clear_screen()
        self.print_correct_guesses()
        print(f"{self.lives_used}/{MAX_LIVES}")
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

        if guess not in self.correct_guesses:
            self.use_life()

    def handle_word_guess(self, guess):
        print("Placeholder")

    def use_life(self):
        self.lives_used += 1

    def is_game_over(self):
        return self.lives_used >= MAX_LIVES

    def is_word_guessed(self):
        return "".join(self.correct_guesses) == "".join(self.word)

    def game_over(self):
        print("Game over.")

    def game_complete(self):
        word = "".join(self.word)
        print("Congratulations! You guessed the word.")
        print(f"The word was {word}")

    def clear_screen(self):
        print("\033[H\033[J", end="")


def main():
    game = Game()
    game.start()


main()
