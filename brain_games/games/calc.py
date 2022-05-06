from random import randint, choice


GAME_RULES = 'What is the result of the expression?'


def get_question_and_answer():
    operator = choice('+-*')
    random_number1 = randint(1, 10)
    random_number2 = randint(1, 10)
    question = f'{random_number1} {operator} {random_number2}'
    correct_answer = ''
    if operator == '+':
        correct_answer = str(random_number1 + random_number2)
    elif operator == '-':
        correct_answer = str(random_number1 - random_number2)
    elif operator == '*':
        correct_answer = str(random_number1 * random_number2)
    return question, correct_answer
