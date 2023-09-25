#!/usr/bin/python3

import sys

data = __import__('data')

"""
function to print out available resources

function to get order, validate/process the order and return the order output

function to validate the available resource and return if transaction is possible or not

function to take payments in coin and return the total amount of coin

function to process the order, and reset the resource if needed

function to organize other functions to get it to behave as needed

"""

def report(resource, balance):
    print(f"available resources : {resource}")
    print(f'total available balance: ${balance}')


def off():
    print('exiting...')
    sys.exit(0)

def get_order(menu, func, func2):
    print(f"coffee and there prices: {item for item in menu}")
    order = input(('Enter your coffee choice(espresso/latte/cappuccino) : '))
    if order in menu:
        result = menu[order]
        return order, result
    elif order.lower() == 'report':
        func(data.resources, data.profit)
    elif order.lower() == 'off':
        func2()

def check_resources(order, resource):
    for item in resource:
        if resource[item] >= order['ingredients'][item]:
            continue
        else:
            print(f'not enough {item}')
            return False
    return True

def receive_payment():
    pay = 0

    print('insert your payment in coins')
    pay += int(input('How many quarters: ')) * 0.25
    pay += int(input('How many dimes: ')) * 0.10
    pay += int(input('How many nickles: ')) * 0.05
    pay += int(input('How many pennies: ')) * 0.01

    return pay

def process_order(resources, order, payment):

    if payment == order[1]['cost']:
        print(f"here's your cup of {order[0]}")
        data.profit += order[1]['cost']
        for item in resources:
            resources[item] -= order[1]['ingredients'][item]
    elif payment > order[1]['cost']:
         print(f"here's your cup of {order[0]}")
         print(f"here's is ${payment - order[1]['cost']:.2f} in change")
         data.profit += order[1]['cost']
         for item in resources:
             resources[item] -= order[1]['ingredients'][item]
    else:
        print('not enough money')
        print('take back your money')

def main():
    order = get_order(data.MENU, report, off)
    if type(order ) == tuple:
        state = check_resources(order[1], data.resources)
        if state == True:
            pay = receive_payment()
            process_order(data.resources, order, pay)

if __name__ == '__main__':
    play = True
    while play:
        main()

