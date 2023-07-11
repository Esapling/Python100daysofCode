from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface


question_bank = []
for question in question_data:
    qstObj = Question(question["question"], question["correct_answer"], question["category"], question["difficulty"])
    question_bank.append(qstObj)

quiz = QuizBrain(question_bank)


quizInt = QuizInterface(quizbrain=quiz)

