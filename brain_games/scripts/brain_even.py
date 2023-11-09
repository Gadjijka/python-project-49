import random
import sys
import prompt
from brain_games import cli


def main():
   cli.welcome_Tirion()
   print("Welcome to the Brain Games!")
   name = cli.welcome_user()
   print("Answer 'yes' if the number is even, otherwise answer 'no'")
   i=0
   while i<3:
       number=random.randint(0,100)
       print('Question:', number)
       answer=prompt.string('Your Answer:')
       if answer!='no' and answer!='yes':
          print("Incorrect answer. Let's try again")
          sys.exit()
       if number%2==0:
          if answer=='yes':
             print('Correct!')
             i+=1
             continue
          else:
             print("'no' is wrong answer ;(. Correct answer was 'yes'."
                   "Let's try again," + " " + name + '!')
             sys.exit()
       else:
          if answer=='no':
             print('Correct!')
             i+=1
             continue
          else:
             print("'yes' is wrong answer ;(. Correct answer was 'no'."
                   "Let's try again," + name +'!')
             sys.exit()
   print("Congratulations,"+name+'!')


if __name__ == 'main':
    main()
