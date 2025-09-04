MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 1.print report of all the machine resources


def report(resource):
    milk = resource['milk']
    coffee = resource['coffee']
    water = resource['water']
    return print('Report: \n' + f'coffee:{coffee}\n' + f'milk:{milk}\n' + f'water:{water}\n')


# TODO: 2.print menu

def menu(MENU):
    espresso = MENU['espresso']['cost']
    cappuccino = MENU['cappuccino']['cost']
    latte = MENU['latte']['cost']
    return print('menu:\n', f'espresso:${espresso}\n', f'cappuccino:${cappuccino}\n', f'latte:${latte}')


# TODO: 3.Take the order from the customer
def order():
    buyer_order = {}
    request = input('what is Your order?').lower()
    if request == 'report':
        print(resources)
        return False
    elif request == 'off':
        return True
    elif request in MENU:
        buyer_order['coffee'] = MENU[request]["ingredients"]['coffee']
        buyer_order['milk'] = MENU[request]['ingredients']['milk']
        buyer_order['water'] = MENU[request]['ingredients']['water']
        buyer_order['cost'] = MENU[request]['cost']
        return buyer_order


# TODO: 4.Check if the resources are enough
def resource_check(resource_in, ordered, ):
    new_resources = {}

    if ordered != 0:
        milk = resource_in['milk']
        coffee = resource_in['coffee']
        water = resource_in['water']

        orderedmilk = ordered['milk']
        orderedcoffee = ordered['coffee']
        orderedwater = ordered['water']

        if orderedcoffee > coffee:
            print('sorry there are limited resources in the machine we cant help you right now :( ')
            return False
        elif orderedmilk > milk:
            print('sorry there are limited resources in the machine we cant help you right now :( ')
            return False
        elif orderedwater > water:
            print('sorry there are limited resources in the machine we cant help you right now :( ')
            return False
        else:

            milk -= orderedmilk
            water -= orderedwater
            coffee -= orderedcoffee
            new_resources['milk'] = milk
            new_resources['water'] = water
            new_resources['coffee'] = coffee

            return new_resources
    else:
        return False


# TODO: 5.check if the given money is enough


def payment_check(order):
    if order != 0:
        money = {'quarter': 0.25, 'dimes': 0.10, 'nickle': 0.05, 'penny': 0.01}
        cost = order['cost']
        q = (float(input('how many quarters?:'))) * money['quarter']
        d = float(input('how many dimes?:')) * money['dimes']
        n = float(input('how many nickles?:')) * money['nickle']
        p = float(input('how many pennies?:')) * money['penny']
        payment = float(q + d + n + p)
        if payment <= cost:

            print(f'Sorry that\'s not enough money :{round(payment, 2)}.money refunded')
            return False
        else:
            change = float(payment - cost)
            print('here is your coffee')
            print(
                f'Total payment :${round(cost, 2)} ,You payed ${round(payment, 2)} ,Here is your change :${round(change, 2)}')
            return True


def new_resources(used_res):
    resources['milk'] -= used_res['milk']
    resources['water'] -= used_res['water']
    resources['coffee'] -= used_res['coffee']

    return resources


def main():
    machine = 1

    while machine == 1:
        print('----------------------------\nWelcome to the coffee oxO machine\n ----------------------------------- ')
        menu(MENU)
        order_info = order()
        if order_info == True:
            machine = 0
        else:
            if resource_check(resources, order_info) != False:
                if payment_check(order_info) == True:
                    new_resources(order_info)
                machine = 1


main()
