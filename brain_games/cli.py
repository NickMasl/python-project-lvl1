"""greeting User prompt."""

import prompt  # importing F to identify user


def welcome_user():
    """Greeting function."""
    print('Welcome to the Brain games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
