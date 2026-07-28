import random

#create a list of most common english yes no starters
yes_no_starters = ["Am", "Is", "Are", "Was", "Were", "Do", "Does", "Did", "Have", "Has", "Had", 
    "Can", "Could", "Will", "Would", "Shall", "Should", "May", "Might", "Must", 
    "Ought", "Dare", "Need", "Aren't", "Isn't", "Wasn't", "Weren't", "Don't", 
    "Doesn't", "Didn't", "Haven't", "Hasn't", "Hadn't", "Can't", "Couldn't", 
    "Won't", "Wouldn't", "Shouldn't", "Mayn't", "Mightn't", "Mustn't", "Oughtn't", 
    "Daren't", "Needn't", "Ya", "You", "Gonna", "Wanna", "Got", "Ever", "See", 
    "Hear", "Mind", "Care", "Innit", "Eh"]

PlayAgain = str('Y')
#print(PlayAgain)

while PlayAgain == str('Y'):
    #print(PlayAgain)
    Question = input('I am the Magic 8 Ball.  I know all.  Ask me any Yes/No question.')
  


# Check in the question starts with one of the first word starters. 
# Create a variable of just the first word
    First_Word = Question.split()[0]
    #print(First_Word)
#Make the first word vaiable a title to match the starters list.
    First_Word_Title = First_Word.title()
    #print(First_Word_Title)
#check if the first word is in the starters list
    Is_Starter = First_Word_Title in yes_no_starters

# if it's in the list create a random number between 1-6 and print the cooresponding response
    if Is_Starter:
        Result = random.randint(1,6)
        print("You asked: ", Question)
        print('May answer is: ')
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
    else: 
        print('That was not a Yes/No question!')
#Ask to play again, if Y or Yes continue while loop
    PlayAgain = str(input('Would you like to Play Y/N'))
    PlayAgain = PlayAgain.capitalize()
   
print('Thanks for Playing!')