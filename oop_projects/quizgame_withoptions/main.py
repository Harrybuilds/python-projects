from data import questions_data
from quiz_model import QuizWithOptions
from question_model import Question
from random import randrange

question_bank = []
for item in questions_data:
    question = item['question']
    answer = item['correct_answer']
    options = item['incorrect_answers']
    num = randrange(4)
    options.insert(num, answer)
    question_object = Question(question, answer, options)
    question_bank.append(question_object)


quizobj = QuizWithOptions(question_bank)

while quizobj.question_number < len(quizobj.question_list):
    quizobj.next_question()
    print(f'Your current score = {quizobj.score}/{quizobj.question_number}')
    print()
    
print(f"Your final score {quizobj.score}")
