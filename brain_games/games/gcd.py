from random import randint
from math import gcd


GAME_RULES = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    correct_answer = str(gcd(random_number1, random_number2))
    question = f'{random_number1} {random_number2}'
    return question, correct_answer
