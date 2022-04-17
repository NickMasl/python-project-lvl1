#!/usr/bin/env python3
"""Even game."""

import prompt
from random import randint


def main():
    greeting = 'Welcome to the Brain Games!'
    return greeting


print(main())


name = prompt.string('May I have your name? ')


def welcome_user():
    return 'Hello, {}!'.format(name)


print(welcome_user())

random_number = randint(1, 100)


def start_game():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def ask_question():
    return 'Question: {}'.format(random_number)


print(start_game())


def is_even(random_number):
    return 'yes' if random_number % 2 == 0 else 'no'


def ask_even():
    random_number = randint(1, 100)
    is_even(random_number)
    print(ask_question())
    answer = prompt.string('Your answer: ')
    wrong_message = "'{}' is wrong answer ;(. Correct answer was '{}'.\nLet's try again, {}!".format(answer, is_even(random_number), name)
    right_message = 'Correct!'
    win_message = 'Congratulations, {}!'.format(name)
    result = ''
    i = 0
    while i < 3:
        print(ask_question())
        if is_even(random_number) == answer:
            result +=  right_message
        else:
            return wrong_message
        i = i + 1 
    return win_message


print(ask_even())


if __name__ == '__main__':
    main()
