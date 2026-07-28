import random

 
#Create a function for the 8ball question, generates a random number and returns an answer based on the random number
#Positive answers print Green, Nutral print Yellow and Negative print red.
# Using the built in Python Ansi codes for color.   \033[32m is Green, \033[31m is Red, \033[33m is Yellow \033[0m resets formatting
def Ball():
    Result = random.randint(1,20)
    if Result == 1:
        Answer = "\033[32m It is certain \033[0m "
    if Result == 2:
        Answer = "\033[32m It is decidedly so \033[0m "
    if Result == 3:
        Answer = "\033[32m Without a doubt \033[0m "
    if Result == 4:
        Answer = " \033[31mDon't count on it \033[0m "
    if Result == 5:
        Answer = '\033[31m My reply is no \033[0m '
    if Result == 6:
        Answer = '\033[32m Yes definitely \033[0m '
    if Result == 7:
        Answer = '\033[31m Very doubtful \033[0m '
    if Result == 7:
        Answer = '\033[32m You may rely on it \033[0m '
    if Result == 9:
        Answer = '\033[32m As I see it, yes \033[0m '
    if Result == 10:
        Answer = '\033[32m Most likely \033[0m '
    if Result == 11:
        Answer = '\033[32m Outlook good \033[0m '
    if Result == 12:
        Answer = '\033[32m Yes \033[0m '
    if Result == 13:
        Answer = '\033[32m Signs point to yes \033[0m '
    if Result == 14:
        Answer = '\033[33m  Reply hazy, try again \033[0m '
    if Result == 15:
        Answer = '\033[33m  Ask again later \033[0m '
    if Result == 16:
        Answer = '\033[33m  Better not tell you now \033[0m '
    if Result == 17:
        Answer = '\033[33m  Cannot predict now \033[0m '
    if Result == 18:
        Answer = '\033[33m  Concentrate and ask again \033[0m '
    if Result == 19:
        Answer = '\033[31m Outlook not so good \033[0m '
    if Result == 20:
        Answer = '\033[31m My sources say no \033[0m '
    return Answer

#create a list of most common english yes no starters
yes_no_starters = ["Am", "Is", "Are", "Was", "Were", "Do", "Does", "Did", "Have", "Has", "Had", 
    "Can", "Could", "Will", "Would", "Shall", "Should", "May", "Might", "Must", 
    "Ought", "Dare", "Need", "Aren't", "Isn't", "Wasn't", "Weren't", "Don't", 
    "Doesn't", "Didn't", "Haven't", "Hasn't", "Hadn't", "Can't", "Couldn't", 
    "Won't", "Wouldn't", "Shouldn't", "Mayn't", "Mightn't", "Mustn't", "Oughtn't", 
    "Daren't", "Needn't", "Ya", "You", "Gonna", "Wanna", "Got", "Ever", "See", 
    "Hear", "Mind", "Care", "Innit", "Eh"]

PlayAgain = str('Y')


while PlayAgain == str('Y'):
    
  #I was getting a index error if I left the question blank so this makes sure it's not blank.  
    while True:
        Question = input('I am the Magic 8 Ball.  Ask me any Yes/No question.')
        if Question == "":
            print("Error: Input cannot be left blank! Please try again.")
        else:
            break

    print("You asked: ", Question)


# Check if the question starts with one of the first word starters. 
# Create a variable of just the first word
    First_Word = Question.split()[0]
#Make the first word vaiable title case to match the starters list.
    First_Word_Title = First_Word.title()

#if the first word is in the starters list run the 8_Ball function, if not Say its not a yes no question
    
    Is_Starter = First_Word_Title in yes_no_starters

# if it's in the list create a random number between 1-6 and print the cooresponding response
    if Is_Starter:
        print("The Magic 8-Ball says:" , Ball())
    else: 
        print('That was not a Yes/No question!')
#Ask to play again, if Y continue while loop if anything else exit and end
    PlayAgain = str(input("Press Y to ask another question.  Or press any other key to stop."))
    PlayAgain = PlayAgain.capitalize()
    
   
print('Thanks for Playing!')