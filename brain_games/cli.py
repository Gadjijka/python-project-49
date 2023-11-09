import prompt

def welcome_Tirion():
    print('Hello, Tirion')

def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello', name)
    return name
