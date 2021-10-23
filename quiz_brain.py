class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.queList = question_list
        self.score = 0

    def has_more_que(self):
        if len(self.queList) > self.question_number:
            return True
        else:
            return False

    def next_question(self):
        current_question = self.queList[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}:  {current_question.text} (True/ False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            self.score += 1
            print("     You got it right!")
        else:
            print("     You got wrong")
        print(f"    The correct answer was {current_answer}")
        print(f"    your current score is: {self.score}/{self.question_number}")
        print("\n")
