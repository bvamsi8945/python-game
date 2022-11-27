import random
import time

score=0
def main():
    '''Main function'''
    print('Welcome to the dice rolling game!')
    dice=random.randint(1,6)
    while True:
        try:
            number = int(input('Enter a number between 1 and 6: '))
            if number < 1 or number > 6:
                print('Number must be between 1 and 6!')
                continue
            break
        except ValueError:
            print('Invalid input!')
            continue
    print('Rolling the dice...')
    time.sleep(2)
    print('The value is:', dice)
    if dice == number:
        global score
        score+=1
        print('You win!, your score is',score)
    else:
        print('You lose!')
        print('Better Luck next time')
while True:
    main()