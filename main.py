from data import question_data
from question_model import Question
import quiz_brain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))


quiz = quiz_brain.QiuzBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You was finished the quiz.")
print(f"You score is: {quiz.score}/{len(quiz.question_list)}")
