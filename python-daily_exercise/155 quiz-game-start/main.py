#!/usr/bin/env python3
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))


# TODO: Asking the questions
# TODO: Checking if the answer was correct
# TODO: Checking if we're at the end of the quiz

quize = QuizBrain(question_bank)

while quize.still_has_question():
    quize.next_question()


print("You've completed the quiz")
