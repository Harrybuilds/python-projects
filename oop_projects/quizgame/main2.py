from data import question_data
from question_model2 import Question
from quiz_model2 import Quiz


question_bank = []
for item in question_data:
    question = item["question"]
    answer = item['correct_answer']
    quest = Question(question, answer)
    question_bank.append(quest)


quiz = Quiz(question_bank)

"""
This code snippet can be used in replacement for the should_continue method


while quiz.question_number < len(quiz.question_list):
quiz.next_question()
"""
while quiz.should_continue():
    quiz.next_question()
print(f"{quiz.score=}/{quiz.question_number}")
