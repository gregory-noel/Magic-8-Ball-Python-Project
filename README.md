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

The first attempt work as it should but I have a few ideas to improve it
1. Uppercase the response to play again in case someone uses a small y.
2. all Yes to play again in case someone types yes instead of just y
3. accept Y, N, Yes, or No  for play again and if not says invalid answer and asks again.
4. ensure the input is a yes no question.  such as check the first work of the sentence to ensure its an Auxilary verb such as "am, can, will etc"  This would mean creating a list of accepted verbs and then verifying the first word of the question is in the list


2nd version I added a list of common verbs to ensure it was a typical yes/no question. and checked the typed question agains the list before proceeding

