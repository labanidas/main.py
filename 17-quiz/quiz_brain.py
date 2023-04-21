class Quiz:

    def __init__(self, question_b):
        self.question_number = 0
        self.question_list = question_b
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        curr = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q{self.question_number}.{curr.text} (True/False)? ").capitalize()
        # print(self.question_number)
        self.check_answer(user_ans, curr.answer)

    def check_answer(self, user_ans, curr_ans):
        if user_ans == curr_ans:
            print("You got it!")
            self.score += 1
        else:
            print("You're wrong!")
        print(f"The correct answer was {curr_ans}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
