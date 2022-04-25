#!/usr/bin/env python3
"""Even game."""


import prompt
from random import randint, choice


def main():
    greeting = 'Welcome to the Brain Games!'
    return greeting


print(main())


name = prompt.string('May I have your name? ')


def welcome_user():
    return 'Hello, {}!'.format(name)


print(welcome_user())


def ask_even():  # noqa: C901
    def start_game():
        return 'What is the result of the expression?'
    print(start_game())
    right_message = 'Correct!'
    win_message = 'Congratulations, {}!'.format(name)
    i = 0
    while i < 3:
        rd1 = randint(1, 10)
        rd2 = randint(1, 10)
        operator = choice('+-*')

        def ask_question():
            return 'Question: {} {} {}'.format(rd1, operator, rd2)
        print(ask_question())
        answer = prompt.string('Your answer: ')

        def solve():
            if operator == '+':
                return rd1 + rd2
            elif operator == '-':
                return rd1 - rd2
            elif operator == '*':
                return rd1 * rd2

        wrong_message = ("'{}' is wrong answer ;( Correct answer was '{}'.\n Let's try again, '{}'!").format(answer, solve(), name)  # noqa: E501

        if solve() == int(answer):
            print(right_message)
        else:
            return wrong_message
        i = i + 1
    return win_message


print(ask_even())


if __name__ == '__main__':
    main()
