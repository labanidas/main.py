from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []

for question in question_data:
    que = question["text"]
    ans = question['answer']
    new_que = Question(que, ans)
    question_bank.append(new_que)

new_quiz = Quiz(question_bank)

while new_quiz.still_has_questions():
    new_quiz.next_question()

print("You completed the quiz!")
print(f"Your final score is {new_quiz.score}/{new_quiz.question_number}")
