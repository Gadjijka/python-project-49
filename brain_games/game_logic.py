import prompt


def play_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)

    for _ in range(3):
        question, right_answer = game.generate_round()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer."
                f"Correct answer was '{right_answer}'."
                f"\nLet's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
