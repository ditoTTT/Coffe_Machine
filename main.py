MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "money": 0
}

big_process = True
while big_process:
    process_order = True
    question = input('What would you like? (espresso,latte,cappuccino): ').lower()
    def recieve_order():
        """get order, and return it's ingredients"""
        global process_order
        if question == 'report':
            for res, amnt in resources.items():
                print(res, amnt)
                process_order = False
        else:
            return MENU[question]
    order = recieve_order()
    while process_order:
        money_loop = True
        def check_res(type_of_coffe):
            """check if there's enough resources to proceed"""
            global process_order
            global money_loop
            yes_no = 0
            for res, amnt in type_of_coffe['ingredients'].items():
                if resources[res] > amnt:
                    yes_no = 1
                else:
                    print(f'Sorry Theres Not Enough {res}')
                    yes_no = 0
                    money_loop = False
                    process_order = False
            return yes_no
        check_resource = check_res(order)
        while money_loop:
            def check_money(type_cost):
                """calculate customers money and subtract resources"""
                global money_loop
                global process_order
                quarters = float(input('How many quarters?: ')) * 0.25
                dime = float(input('How many dimes?: ')) * 0.10
                nickel = float(input('How many nickels?: ')) * 0.05
                penny = float(input('How many pennies?: ')) * 0.01
                money = quarters + dime + nickel + penny
                cost = type_cost['cost']
                if money >= cost:
                    print(f'Here is Your Change {round((money - cost), 2)}$\nHere is Your {question}☕☕☕ Enjoy')
                    if 'milk' in type_cost['ingredients']:
                        resources['milk'] = resources['milk'] - type_cost['ingredients']['milk']
                    resources['money'] = resources['money'] + cost
                    resources['water'] = resources['water'] - type_cost['ingredients']['water']
                    resources['coffee'] = resources['coffee'] - type_cost['ingredients']['coffee']
                    process_order = False
                    money_loop = False
                else:
                    print("You don't have enough money")
                    process_order = False
                    money_loop = False
            process = check_money(order)
    

    


        
