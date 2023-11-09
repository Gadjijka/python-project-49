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
        progression=[]
        progression.append(number1)
        number2=random.randint(0,100)
        k=1
        while k<10:
             number1+=number2
             progression.append(number1)
             k+=1
        index=random.randint(0,9)
        temporary_number=progression[index]
        progression[index]=".."
        s=" "
        for char in progression:
              s+=" "+str(char)
        print("Question:"+s)
        answer=prompt.string('Your Answer:')
        if answer != str(temporary_number):
            print("'"+answer+"'"+"is wrong answer ;(. Correct answer was '"+str(temporary_number)+"'.")
            print("Let's try again,"+ " " + name+"!")
            sys.exit()
        print("Correct!")
        i+=1

   print("Congratulations,"+name+'!')


if __name__ == 'main':
    main()
