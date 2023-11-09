import random
import sys
import prompt
from brain_games import cli
import math


def main():
   cli.welcome_Tirion()
   print("Welcome to the Brain Games!")
   name = cli.welcome_user()
   print("Find the greatest common divisor of given numbers.")
   i=0
   while i<3:
        number1=random.randint(0,100)
        number2=random.randint(0,100)
        print("Question:" + str(number1)+" "+ str(number2))
        answer=prompt.string('Your Answer:')
        if answer != str(math.gcd(number1,number2)):
            print("'"+answer+"'"+"is wrong answer ;(. Correct answer was '"+str(math.gcd(number1,number2))+"'.")
            print("Let's try again,"+ " " + name+"!")
            sys.exit()
        print("Correct!")
        i+=1

   print("Congratulations,"+name+'!')


if __name__ == 'main':
    main()
