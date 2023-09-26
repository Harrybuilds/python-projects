# Day 16 of 100 days of code


## Repeating the coffee machine using object oriented programing in python
  
## NOTE:
- all classes were already defined in the 100 days of code program


### classes and and their attributes used  
- __MenuItem__ - class for creating items to be added to the menu  
  - __methods__  
    - __init__ : instance method that initialises a new MenuItem object  
  - __attributes__  
    * name, water, milk, coffee, cost


- __Menu__ - class for creating object(s) thats has MenuItem objects as it attributes  
  * __methods__
    * __init__ : instance method that initialises a new Menu Object  
    * get_items : instance method to get names of all available items in the menu and return them as a string  
    * find_item : instance method to search and return a MenuItem object in the Menu object if found else returns None  
    * items_list : instance method to get names of all available items in the menu and return them as a list(defined by me)  
  * **attributes**  
	* menu : a list containing MenuItem objects


- __CoffeeMaker__ - for creating object(s) to be used for operating and manipulating the coffee machine.
  * __methods__
    * __init__ : instance method that initialises object(s) of CofferMaker class  
    * report : instance method to return the availabe resource in the coffee machine as at when called upon  
    * is_resource_sufficient : instance method to check if resource in coffee machine is enough to for the requested coffee. returns True if resource is sufficient else False   
    * make_coffee : instance method to make the coffee
  * __attributes__  
    - __none__


- __MoneyMachine__ - class for creating object(s) that handles and processes payment. payments are collected in coins
  - __methods__
    - __init__ : instance method that initialises aobject(s) of MoneyMachine class  
    - report : instance method to return the available amount of money as at when called upon  
    - make_payment : instance method to receive payment in coins and process payment. Returns True is payment is enough for the coffee to be purchased else False  
    - process_coin : instance method that is called within the make_payment method. It takes payments in conins from the keyboard  
  - __attributes__  
    - CURRENCY : class constant attribute that represent the currency  
    - COIN_VALUES : class constant attribute that represent the values of each coin  
