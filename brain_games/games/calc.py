from random import randint, choice


GAME_RULES = 'What is the result of the expression?'


def get_question_and_answer():
    operator = choice('+-*')
    random_digit1 = randint(1, 10)
    random_digit2 = randint(1, 10)
    question = '{} {} {}'.format(random_digit1, operator, random_digit2)
    if operator == '+':
        correct_answer = str(random_digit1 + random_digit2)
        return question, correct_answer
    elif operator == '-':
        correct_answer = str(random_digit1 - random_digit2)
        return question, correct_answer
    elif operator == '*':
        correct_answer = str(random_digit1 * random_digit2)
        return question, correct_answer
