#!/bin/env python
import json
import random
import requests

DIFFICULTIES = ["easy", "normal", "hard"]
DIFFICULTIES_STR = ", ".join(DIFFICULTIES)
MAX_STAGE = 10


class Game:
    difficulty = None
    word = None
    correct_letters = None
    guessed_letters = []
    stage = 1

    def __init__(self):
        self.difficulty = self.__get_difficulty()
        self.word = self.__generate_word()
        self.word = list(self.word)
        self.correct_letters = ["_"] * len(self.word)

    def begin(self):
        while True:
            if self.stage >= MAX_STAGE:
                self.__game_over()
                break
            elif "".join(self.correct_letters) == "".join(self.word):
                self.__game_complete()
                break

            self.__print_ui()

            guess = self.__get_guess()
            self.__check_guess(guess)

    def __print_ui(self):
        correct_guesses = "".join(self.correct_letters)
        guessed_letters = ", ".join(self.guessed_letters)
        self.__clear()
        print(f"Correct guesses: {correct_guesses}")
        print(self.__get_stickman())
        print(f"{self.stage}/{MAX_STAGE}")
        print(f"Guessed letters:\n{guessed_letters}")

    def __get_guess(self):
        while True:
            guess = input("What's your guess? ").lower()
            if not guess.isalpha():
                print("Please only guess letters!")
                continue
            elif guess in self.guessed_letters:
                print("That has already been guessed!")
                continue

            return guess

    def __clear(self):
        print("\033[H\033[J", end="")

    def __get_stickman(self):
        match self.stage:
            case 1:
                return """








"""
            case 2:
                return """







______
"""
            case 3:
                return """

|
|
|
|
|
|
|_____
"""
            case 4:
                return """
 _____
|
|
|
|
|
|
|_____
"""
            case 5:
                return """
 _____
|     |
|     O
|
|
|
|
|_____
"""
            case 6:
                return """
 _____
|     |
|     O
|     |
|
|
|
|_____
"""
            case 7:
                return """
 _____
|     |
|     O
|    /|
|
|
|
|_____
"""
            case 8:
                return """
 _____
|     |
|     O
|    /|\\
|
|
|
|_____
"""
            case 9:
                return """
 _____
|     |
|     O
|    /|\\
|    /
|
|
|_____
"""
            case _:
                return """
 _____
|     |
|     O
|    /|\\
|    / \\
|
|
|_____
"""

    def __check_guess(self, guess):
        if len(guess) == 1:
            return self.__check_letter_guess(guess)
        else:
            return self.__check_word_guess(guess)

    def __check_letter_guess(self, guess):
        self.guessed_letters.append(guess)
        for idx, letter in enumerate(self.word):
            if letter == guess:
                self.correct_letters[idx] = guess

        if guess not in self.correct_letters:
            self.__next_stage()

    def __check_word_guess(self, guess):
        if guess == "".join(self.word):
            self.correct_letters = list(self.word)

        if guess != self.word:
            self.__next_stage(2)

    def __game_over(self):
        self.__clear()
        word = "".join(self.word)
        print("Game over!")
        print(f"The word was {word}!")
        print(self.__get_stickman())

    def __game_complete(self):
        self.__clear()
        word = "".join(self.word)
        print("Congratulations!")
        print(f"The word was {word}!")
        print(self.__get_stickman())

    def __next_stage(self, stages_to_increment=1):
        self.stage += stages_to_increment

    def __get_difficulty(self):
        while True:
            difficulty = input(
                f"What difficulty would you like to use? ({DIFFICULTIES_STR}) "
            ).lower()

            if difficulty not in DIFFICULTIES:
                print("That is not an available difficulty!")
                continue

            match difficulty:
                case "easy":
                    return 4
                case "normal":
                    return 6
                case "hard":
                    return 10

    def __generate_word(self):
        response_raw = requests.get(
            "https://random-word-api.herokuapp.com/word" +
            "?number=1" +
            f"&length={self.difficulty}")

        response_json = json.loads(response_raw.text)[0]
        return response_json


Game().begin()
