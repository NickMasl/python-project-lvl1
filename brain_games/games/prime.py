from random import randint


game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    new_number = int(str(number)[-2:])
    if new_number == 0:
        return 'no'
    i = 2
    while i < new_number:
        if new_number % i == 0:
            return 'no'
        i = i + 1
    return 'yes'

def get_question_and_answer():
    question = randint(1, 10000)
    correct_answer = 'yes' if is_prime(question) == 'yes' else 'no'
    return question, correct_answer