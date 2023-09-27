# Quiz game with multiple options to pick from, built using OOP learnt from 100 days of code by Dr Angela Yu

## Decided to test my understanding of OOP in python, then engaged in building a modified version of the quiz game built using OOP in the 100 days days code course by Dr. Angela Yu  
## Day 17

### Classes and their attributes(methods and variables)
    - Question
    Template of Question object(s) should be
    
      - _methods_
      	_ __init__ : instance method that initialises Question object(s) when created
	
      - _attributes_
      	- __question__ : instance variable used to hold the question itself
	- __answer__ : instance variable used to hold the correct answer to the question
	- __options__ : instance variable list used to hold possible answers to the question
	
    - QuizWithOptions
    Template for how QuizWithOptions object(s) should be
    
      - _methods_
      	- __init__ : instance method used initialise QuizWithOptions object(s) when created
	- __next_question__ : instance method used to pick the next question, print the question, get a reply in character and then process the reply
	- __check_answer__ : instance method used to check if reply is correct or not
	- __march_answer__ : instance method used to convert user reply in character to the corresponding string
	
      - _attributes_
      	- __question_number__: instance variable used to track the next question to be asked
	- __score__: instance variable used to track the number of correctly answered questions
	- __question_list__: instance variable used to hold a list of all the question to be asked
      
### Question_bank
- questions gotten from the Open Trivia Database as json objects, using the Open Trivia Database API

### Python Builtin Data structures used
    - **List**
    - **Dictionary**

### Python Builtin Modules and functions used
    - random
      - _functions_
      	- __randrange__

### Python concept used
    - __OOP__
    - __Loops__
    - __Identifiers__
    - __functions__
    