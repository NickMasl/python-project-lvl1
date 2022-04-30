from random import randint, choice


game_rules = 'What is the result of the expression?'


def get_question_and_answer():
    operator = choice('+-*')
    rd1 = randint(1, 10)
    rd2 = randint(1, 10)

    def solve():
        if operator == '+':
            return rd1 + rd2
        elif operator == '-':
            return rd1 - rd2
        elif operator == '*':
            return rd1 * rd2
    correct_answer = str(solve())
    question = '{} {} {}'.format(rd1, operator, rd2)
    return question, correct_answer
