"""greeting User prompt."""

import prompt  # importing F to identify user


def welcome_user():
    """Greeting function."""
    name = prompt.string('May I have your name? ')
    message = 'Hello, ' + name + '!'
    print(message)
