from random import randint, choice


GAME_RULES = 'What is the result of the expression?'


def get_question_and_answer():
    operator = choice('+-*')
    random_digit1 = randint(1, 10)
    random_digit2 = randint(1, 10)

    def solve():
        if operator == '+':
            return random_digit1 + random_digit2
        elif operator == '-':
            return random_digit1 - random_digit2
        elif operator == '*':
            return random_digit1 * random_digit2
    correct_answer = str(solve())
    question = '{} {} {}'.format(random_digit1, operator, random_digit2)
    return question, correct_answer
