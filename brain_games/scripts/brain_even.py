#!/usr/bin/env python3
"""Even game."""


import prompt
from random import randint


def main():
    greeting = 'Welcome to the Brain Games!'
    return greeting


name = prompt.string('May I have your name? ')


def welcome_user():
    return 'Hello, {}!'.format(name)


print(welcome_user())


def ask_even():
    def start_game():
        return 'Answer "yes" if the number is even, otherwise answer "no".'
    print(start_game())
    right_message = 'Correct!'
    win_message = 'Congratulations, {}!'.format(name)
    i = 0 
    while i < 3:
        random_number = randint(1, 100)
        def ask_question():
            return 'Question: {}'.format(random_number)
        print(ask_question())
        answer = prompt.string('Your answer: ')
        def is_even(random_number):
            return 'yes' if random_number % 2 == 0 else 'no'
        wrong_message = "'{}' is wrong answer ;(. Correct answer was '{}'.\nLet's try again, {}!".format(answer, is_even(random_number), name)
        if is_even(random_number) == answer:
            print(right_message)
        else:
            return wrong_message
        i = i + 1
    return win_message


print(ask_even())


if __name__ == '__main__':
    main()
