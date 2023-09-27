# Day 17 of 100 days of code, by Dr. Angela Yu  

## Quiz game built using oop in python  

### Recreated the quiz game  

### Classes and their attributes(methods and variables)
- __Question__ : models how a Question object(s) should be like
  - _methods_
    - __init__: instance method that initialises object(s) of Question class when created
    - _attributes_
      - __question__ : instance attribute that holds the question itself in string representation
      - __answer__ : instance attribute that holds the correct answer to the question in string representation


- __Quiz__ : models how a Quiz object(s) should be like
  - _methods_
    - __init__ : instance method that initialises object(s) of the Quiz class when created
    - __next_question__ : instance method that picks a question, ask the question to get a reply, and process the reply
    - __check_answer__ : instance method that evaluate the reply to the question reply
    - __should_continue__ : instance method that checks if there's more question to be asked or not. NOTE: the quiz game can work just fine without using this method
 - _attributes_
   - question_number : instance attribute that holds the number of the next question to be asked
   - question_list : instance attribute that holds a list containing question objects
   - score : instance attribute that holds the total number of correct answer gotten from answering the question


### Question bank
A list containing  dictionaries of data from which the question object data is picked and the question object is created