class QuizWithOptions:

    """ Template for object(s) of QuizWithOption class """

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.possible_answers = ['A','B','C','D']

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"Q{self.question_number}: {current_question.question}")
        answer = input(f"A. {current_question.options[0]}  B. {current_question.options[1]}\nC. {current_question.options[2]}  D. {current_question.options[3]} (pick an option): ")
        
        while answer.upper() not in self.possible_answers:
            print('\nplease pick an option from the available options(A,B,C,D)')
            answer = input(f"A. {current_question.options[0]}  B. {current_question.options[1]}\nC. {current_question.options[2]}  D. {current_question.options[3]} (pick an option): ")
            
        status = self.check_answer(answer, current_question.answer, current_question.options)
        

    def march_answer(self, answer, answer_options):
        if answer.upper() == 'A':
            answer = answer_options[0]
        elif answer.upper() == 'B':
            answer = answer_options[1]
        elif answer.upper() == 'C':
            answer = answer_options[2]
        else:
            answer = answer_options[3]

        return answer
    
    def check_answer(self, answer, correct_answer, answer_options):
        result = self.march_answer(answer, answer_options)
        if result == correct_answer:
            print("You're right")
            self.score += 1
            return True
        print(f"You failed it, the correct answer is {correct_answer}")
        return False
