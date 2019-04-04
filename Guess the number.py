from random import*
anwser = randint(1, 100)
tries = 0
prizes = ['$1000 gift card', 'computer', 'iphone', 'furniture', 'painting', 'macbook', 'ipad']
prizes2 = ['coffee', 'donut', '$100gift card', 'tablet', 'free drinks', 'free meal']
prize = sample(prizes, 1)
prize2 = sample(prizes2, 1)
print(prize2)
print('This is a guessing game and you need to guess a number between 1 and 100')

question = input("Would you like to play? [y/n] ")

if question != "y":
    print('maybe next time')

if question == 'y':
    guess = int(input('Guess number: '))
    if anwser < guess:
        print('Guess lower')
        tries += 1
    if anwser > guess:
        print("Guess Higher")
        tries += 1
    if guess == anwser:
        print('You win!!!')
    while guess != anwser:
        guess = int(input('Guess number: '))
        if anwser < guess:
            print('Guess lower')
            tries += 1
        if anwser > guess:
            print("Guess Higher")
            tries += 1
    if guess == anwser:
        print('You win!!!')
        if 3 < tries < 10:
            print('You win a ')
        if tries < 1:
            print('Champion, you win a house')
        if tries == 2:
            print('almost perfect you win a car')
        if tries == 3:
            print('awesome you win a vacation')
        if 3 < tries <= 5:
            print(prize)
        if 5 < tries < 10:
            print(prize2)
        if tries < 10:
            print('good job')
