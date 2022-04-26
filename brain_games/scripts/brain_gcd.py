#!usr/bin/env python3
"""GCD game."""


from random import randint
from math import gcd
import prompt


def main():
    greeting = 'Welcome to the Brain Games!'
    return greeting


print(main())


name = prompt.string('May I have your name? ')


def welcome_user():
    return 'Hello, {}!'.format(name)


print(welcome_user())


def ask_gcd():
    def start_game():
        return 'Find the greatest common divisor of given numbers.'
    print(start_game())
    right_message = 'Correct!'
    win_message = 'Congratulations, {}!'.format(name)
    i = 0
    while i < 3:
        rn1 = randint(1, 100)
        rn2 = randint(1, 100)

        def ask_q():
            return 'Question: {} {}'.format(rn1, rn2)
        print(ask_q())
        answer = prompt.string('Your answer: ')

        def check_answer():
            return gcd(rn1, rn2)

        wrong_message = ("'{} is wrong answer ;(. Correct answer was '{}'.\nLet's try again, {}!").format(answer, check_answer(), name)  # noqa: E501
        if check_answer() == int(answer):
            print(right_message)
        else:
            return wrong_message
        i = i + 1
    return win_message


print(ask_gcd())


if __name__ == '__main__':
    main()
