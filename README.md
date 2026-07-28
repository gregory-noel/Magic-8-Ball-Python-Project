# Magic-8-Ball-Python-Project
A practice project  to create a Magic 8 ball in Python

 
Assignment
Write a program in python that simulates the function of the Magic 8 Ball by printing a response to a user’s question. Please ensure that of the possible responses you have at least 3 from the affirmation answers, 3 from the non-committal and 3 from the negative.

Initial thoughts:
Create a input asking the question
create a list of responses and assign each a number
generate a random number
print the response that relates to the number
ask to play again
if yes ask a new question, if no print a thanks for playing message and end

Thinking a while loop while play again is yes it will ask for a question

The first attempt works as it should but I have a few ideas to improve it

Version 2
1. Uppercase the response to play again in case someone uses a small y.
2. ensure the input is a yes no question.  such as check the first work of the sentence to ensure its an Auxilary verb such as "am, can, will etc"  This would mean creating a list of accepted verbs and then verifying the first word of the question is in the list.

Version 3 
I created a new branch to add a few things:
1. try making the 8 ball responses itself a function to call
2. increased the number of responses to the full 20 from the Og magic 8 ball
3. added some color to the responses based on if they are positive, negative, or neutral.
4. fixed a few errors I was getting such as an index error if the question was blank and ending the game if the person didnt press Y to play again.
5. Updated some of the text messages

Merged the branch to the main branch after I was working correctly.



