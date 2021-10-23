from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    que_text = i["question"]
    que_answer = i["correct_answer"]
    question = Question(que_text, que_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.has_more_que():
    quiz.next_question()
print("You have completed the quiz")
print(f"Your Final score is: {quiz.score}/{quiz.question_number}")
