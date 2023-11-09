import random
import sys
import prompt
from brain_games import cli


def main():
   cli.welcome_Tirion()
   print("Welcome to the Brain Games!")
   name = cli.welcome_user()
   print("What is the result of the expression?")
   i=0
   sum=0
   collection_of_operands=['+','-','*']
   while i<3:
        sign=random.randint(0,2)
        number1=random.randint(100,200)
        number2=random.randint(0,100)
        if sign==0:
            print("Question: " +str(number1) + " + " + str(number2))
            sum=number1+number2
        if sign==1:
            sum=number1-number2
            print("Question: " + str(number1) + " - " + str(number2))
        if sign==2:
            sum=number1*number2
            print("Question: " + str(number1) + " * " + str(number2))
        answer=prompt.string('Your Answer:')
        if answer != str(sum):
            print("'"+str(answer)+"'"+"is wrong answer ;(. Correct answer was '"+str(sum)+"'.")
            print("Let's try again,"+ " " + name+"!")
            sys.exit()
        print("Correct!")
        i+=1

   print("Congratulations, "+name+'!')


if __name__ == 'main':
    main()
