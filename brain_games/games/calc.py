import random

RULES = 'What is the result of the expression?'


def make_expression():
    """
    Generating expression
    """
    list_of_expressions = ['+', '-', '*']
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    operator = random.choice(list_of_expressions)
    right_answer = 0
    match operator:
        case '+':
            right_answer = first_number + second_number
        case '-':
            right_answer = first_number - second_number
        case '*':
            right_answer = first_number * second_number
    return f'{first_number} {operator} {second_number}', right_answer


def generate_round():
    question, right_answer = make_expression()
    return question, str(right_answer)
