# Day 16 of 100 days of code


## Repeating the coffee machine using object oriented programing in python
  
## NOTE:
- all classes were already defined in the 100 days of code program


### classes and and their attributes used  
* __MenuItem__ - for creating items to be added to the menu  
	  *### methods  
	       * ___init__ : instance method that initialises a new MenuItem object  
	  *### attributes
	       * name, water, milk, coffee, cost

* __Menu__ - for creating object(s) thats has MenuItem objects as it attributes
      *### methods
      	   * __init__ : instance method that initialises a new Menu Object  
	   * get_items : instance method to get names of all available items in the menu and return them as a string  
	   * find_item : instance method to search and return a MenuItem object in the Menu object if found else returns None
	   * items_list : instance method to get names of all available items in the menu and return them as a list(defined by me)

      - ### attributes
      	   * menu : a list containing MenuItem objects
      	   
	   
* __CoffeeMaker__ - for creating object(s) to be used for operating and manipulating the coffee machine. 
	   