import random

RULES = 'What is the result of the expression?'


def make_expression():
    """
    Generating expression
    """
    list_of_expressions = ['+', '-', '*']
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    operator = random.choice(list_of_expressions)
    return f'{first_number} {operator} {second_number}'


def generate_round():
    question = make_expression()
    right_answer = str(eval(question))
    return question, right_answer
