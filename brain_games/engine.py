import prompt


NUMBER_OF_ROUNDS = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(game.GAME_RULES)
    for currect_round in range(NUMBER_OF_ROUNDS):
        question, correct_answer = game.get_question_and_answer()
        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;( Correct answer was '{}'.\nLet's try again, {}!".format(answer, correct_answer, name))  # noqa: E501
            return
    print('Congratulations, {}!'.format(name))
