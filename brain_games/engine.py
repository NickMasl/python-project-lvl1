import prompt


number_of_rounds = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(game.game_rules)
    i = 0
    while i < number_of_rounds:
        question, correct_answer = game.get_question_and_answer()
        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;( Correct answer was '{}'.\nLet's try again, {}!".format(answer, correct_answer, name))  # noqa: E501
            return
        i = i + 1
    print('Congratulations, {}!'.format(name))
