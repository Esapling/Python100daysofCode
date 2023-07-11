from data import question_data


class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        print(f"Total number of question is {len(self.question_list)}")
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        return current_question 
        
        #self.check_ans(current_question, ans)
        #print(f"Your current score is {self.score}/{self.question_number}")

    def still_has_question(self):
        if self.question_number >= len(self.question_list):
            return False
        return True
    def check_ans(self, question, user_ans):
        if user_ans == question.ans:
            print("You got it right!")
            self.score += 1
            return True
        else:
            print("Sorry! That is not correct")
            return False

