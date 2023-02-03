from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
# initialize question objects


question_bank = []
for question in question_data:
    qstObj = Question(question["question"], question["correct_answer"], question["category"], question["difficulty"])
    question_bank.append(qstObj)

continue_quiz = True

quiz = QuizBrain(question_bank)
while continue_quiz:
    quiz.next_question()
    if quiz.still_has_question():
        continue_quiz = True
    else:
        continue_quiz = False


print("You have completed the score!")
print(f"Your overall score is {quiz.score} out of {quiz.question_number}")
