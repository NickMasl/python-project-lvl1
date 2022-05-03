from random import randint


GAME_RULES = 'What number is missing in the progression?'


def get_question_and_answer():
    start = randint(1, 10)
    steps = randint(7, 12)
    step = randint(2, 5)
    progression = [str(start)]
    for _ in range(steps):
        progression.append(str(start + step))
        start = start + step
    random_index = randint(0, (len(progression) - 1))
    missing_number = progression[random_index]
    progression[random_index] = str('..')
    question = ' '.join(progression)
    correct_answer = missing_number
    return question, correct_answer
