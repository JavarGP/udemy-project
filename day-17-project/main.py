# this imports files within the same directory 

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain 

# this allows questions to be out within a list 
question_bank = []
for question in question_data:
    question_text = question["text"]
    # this takes the key 'text' from question_data
    question_answer = question["answer"]
    # this takes the key 'answer' from question_data
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    # this put questions that have been asked within  a list 

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Your completed the quiz")
# this is to get the score and i can refeence the quiz obeject and get the score and question number respectively
print(f"Your final score was {quiz.score}/{quiz.question_number}")
