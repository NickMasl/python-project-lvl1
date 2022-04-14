#!/usr/bin/env python3
"""Welcome script."""

from brain_games.cli import welcome_user


def main():
    """Greeting message."""
    greeting = 'Welcome to the Brain Games!'
    print(greeting)


welcome_user()


if __name__ == '__main__':
    main()
