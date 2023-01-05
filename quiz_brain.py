class QiuzBrain:

    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        question_text = current_question.text
        question_answer = current_question.answer
        self.question_number += 1
        correct_answer = False
        while not correct_answer:
            answer = input(f"Q.{self.question_number}: {question_text} ").strip().lower()
            if (answer == "true") or (answer == "false"):
                correct_answer = True
                self.check_answer(answer, question_answer)
            else:
                print("Give correct answer, please!")


    def check_answer(self, user_answer, right_answer):
        if right_answer.lower() == user_answer.lower():
            print("You are right!")
            self.score += 1
        else:
            print("This is wrong!")
        print(f"Right answer: {right_answer.capitalize()}")
        print(f"You score is: {self.score}/{self.question_number}")
        print("\n")

