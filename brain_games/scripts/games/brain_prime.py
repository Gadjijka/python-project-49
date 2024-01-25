import random
import sys
import prompt
from brain_games import cli


def main():
    cli.welcome_Tirion()
    print("Welcome to the Brain Games!")
    name = cli.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        number = random.randint(0, 100)
        print('Question: ' + str(number))
        answer = prompt.string('Your Answer:')
        k = 0
        for r in range(2, number // 2 + 1):
            if number % r == 0:
                k = k + 1
        if k == 0 and answer == 'yes':
            print("Correct!")
            i = i + 1
            continue
        if k > 0 and answer == 'no':
            print("Correct!")
            i = i + 1
            continue
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        print("Let's try again, " + name + '!')
        sys.exit()
    print("Congratulations, " + name + '!')


if __name__ == 'main':
    main()
