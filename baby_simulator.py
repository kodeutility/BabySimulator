#import choice from random
from random import choice

#create a list of questions
questions = ["Why is the sky blue?","Why is there a face on the moon?","Where are dinosaurs?"]

#choose a random question
question = choice(questions)

# store our answer
answer = input(question).strip()

# baby keep asking why till we say "just because" 
while "just because" != answer.strip().lower():
    answer = input("But why?")
print("Oh..Ok")
