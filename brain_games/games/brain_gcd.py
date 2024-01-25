import random

RULES = 'Find the greatest common divisor of given numbers.'


def find_prime_factors(num1, num2):
    """
    Find prime factorials for the number
    """
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def generate_round():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'{num1} {num2}'
    answer = str(find_prime_factors(num1, num2))
    return question, answer
