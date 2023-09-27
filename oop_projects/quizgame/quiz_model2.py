class Quiz:

    """ models how quiz should be like """

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q{self.question_number}: {current_question.question}(true/false): ")
        result = self.check_answer(current_question, answer)
        if result == True:
            self.score += 1

    def check_answer(self, question_object, answer):
        if question_object.answer.lower() == answer.lower():
            print("that's correct\n")
            return True
        print(f"wrong answer, the correct answer is {question_object.answer}\n")
        return False

    def should_continue(self):
        while self.question_number < len(self.question_list):
            return True
        return False

