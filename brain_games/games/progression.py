from random import randint, choice


game_rules = 'What number is missing in the progression?'


def get_question_and_answer():
    start = randint(1, 10)
    steps = randint(7, 12)
    step = randint(2, 5)
    progression = [str(start)]
    i = 0
    while i <= steps:
        progression.append(str(start + step))
        start = start + step
        i = i + 1
    missing_number = choice(progression)
    for i, number in enumerate(progression):
        if number == missing_number:
            progression[i] = str('..')
    question = ' '.join(progression)
    correct_answer = str(missing_number)
    return question, correct_answer
