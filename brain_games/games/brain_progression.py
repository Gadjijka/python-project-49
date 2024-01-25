import random

RULES = 'What number is missing in the progression?'


def make_progression():
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    return [str(start + i * step) for i in range(length)]


def generate_round():
    progression = make_progression()
    index_to_replace = random.randint(0, len(progression) - 1)
    correct_answer = progression[index_to_replace]
    progression[index_to_replace] = '..'
    question = ' '.join(progression)
    return question, correct_answer
