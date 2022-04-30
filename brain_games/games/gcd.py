from random import randint
from math import gcd


game_rules = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    rn1 = randint(1, 100)
    rn2 = randint(1, 100)
    correct_answer = str(gcd(rn1, rn2))
    question = '{} {}'.format(rn1, rn2)
    return question, correct_answer
