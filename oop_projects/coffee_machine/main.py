from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_handler = MoneyMachine()

machine_on  = True

while machine_on:
    order = input(f'which coffee do you want? ({ menu.get_items()}): ')


    if order in menu.items_list():
        order = menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(order):
            if money_handler.make_payment(order.cost):
                coffee_machine.make_coffee(order)
    
    elif order == 'report':
        coffee_machine.report()
        money_handler.report()
        
    elif order == 'off':
        machine_on = False
        
    else:print(f'{order} not available')
    


