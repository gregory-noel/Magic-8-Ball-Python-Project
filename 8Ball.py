import random

PlayAgain = str(input('Would you like to Play Y/N'))
#print(PlayAgain)

while PlayAgain == str('Y'):
    Question = input('I am the Magic 8 Ball.  I know all.  Ask me your question.')
    Result = random.randint(1,6)
    if Result == 1:
        print('It is certain')
    if Result == 2:
        print('It is decidedly so')
    if Result == 3:
        print('Without a doubt')
    if Result == 4:
        print("Don't count on it")
    if Result == 5:
        print('My reply is no')
    if Result == 6:
        print('Very doubtful')

    PlayAgain = input('Play again?  Y/N')