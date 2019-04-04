question = input('Welcome to Madlips. Would you like to play [y/n]')
if question == 'n':
    print('ok you can play later.')


if question == 'y' or 'yes':
    print('In this Madlips you will choose a word that fits the description.')
    n1 = input('Please enter a noun: ')
    p1 = input('Please enter a name: ')
    p2 = input('Please enter a place: ')
    n2 = input('Please enter another noun: ')
    v1 = input('Please enter a verb: ')
    n3 = input('Please enter a noun: ')
    v2 = input('Please enter another verb: ')
    e1 = input('Please enter a emotion: ')
    input('type ready when you want to here the madlip ')
    print('In a city named ' + p2 + ' their was a man ' + v1 + ' down the street and his name was ' + p1 +
          '. While he was ' + v2 + ' a man came up to him ' + n1 + e1 + ' then said ' + n3 + ' then left to ' + n3)
