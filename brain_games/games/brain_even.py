import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    """
    Check if the given number is even.
    """
    return num % 2 == 0


def generate_round():
    number = random.randint(1, 100)
    question = number
    right_answer = 'yes' if is_even(number) else 'no'
    return question, right_answer
