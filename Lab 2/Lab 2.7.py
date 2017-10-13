# Higher or lower? Between 1 and 10.
import random
number = random.randrange(1, 11)
def lets_play():
    guess = input('Your guess?')
    if guess.isnumeric() == False:
        print('Not a number!')
        lets_play()
    elif int(guess) > number:
        print('It\'s lower.')
        lets_play()
    elif int(guess) < number:
        print('It\'s higher.')
        lets_play()
    else:
        print('Correct!')

lets_play()
