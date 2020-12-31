from menu import MENU, resources, coin_values

cash_in_machine=0
total_money_paid=0
go_on=True
# gobal total_money=> can apply inside the functions

# TODO 4. if report. print the result of current resources
def report():
    print(
        f"Water:{resources['water']}ml\nMilk:{resources['milk']}ml\nCoffee:{resources['coffee']}g\nMoney: {cash_in_machine}")

def check_resources(drinks):
    """check whether enough resources to make the drinks"""
#here can use for loop to loop thru each ingredients
    # if check_water<0:
    #     print("Sorry there is not enough water.")
    #     return False
    # elif check_milk<0:
    #     print("Sorry there is not enough milk.")
    #     return False
    #
    # elif check_coffee<0:
    #     print("Sorry there is not enough coffee.")
    #     return False
    #
    # elif check_coffee and check_milk and check_water>=0:
    #     print("Please insert coins.")
    #     return True

    for item in MENU[drinks]["ingredients"]:
        if MENU[drinks]["ingredients"][item]>resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True

def update_resources(used_water,used_milk,used_coffee):
    resources['water'] -= used_water
    resources['milk'] -= used_milk
    resources['coffee'] -= used_coffee




while go_on==True:
    # TODO 1. ask user what would they like
    action = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO 2. 5 replies available, if off then exit
    if action == "off":
        go_on=False

    # TODO 3. 5 replies available, if report then print report
    elif action == "report":
        report()

    # TODO 4. 5 replies available, if order drinks then check resources
    elif action=="espresso" or "latte" or "cappuccino":
        check_water = resources['water'] - MENU[action]['ingredients']['water']
        check_milk = resources['milk'] - MENU[action]['ingredients']['milk']
        check_coffee = resources['coffee'] - MENU[action]['ingredients']['coffee']

        if check_resources(action):

    # TODO 5. if resources available, then ask to insert coins
            for v in coin_values:
                inset_v=int(input(f"How many {v} to insert? "))
                total_money_paid= round(total_money_paid + coin_values[v] * inset_v,2)
                cost = MENU[action]['cost']
            #print(total_money_paid, cost)

    # TODO 6. calculate the coins the user inserted #
    # TODO 7. if excess money offer changes #
    # TODO 8. rerun if not enough money or resources #
            if total_money_paid<cost:
                print("Sorry that's not enough money. Money refunded.")
            elif total_money_paid>=cost:
                change=round(total_money_paid - cost, 2)
                cash_in_machine+=cost
                update_resources(MENU[action]['ingredients']['water'],MENU[action]['ingredients']['milk'],MENU[action]['ingredients']['coffee'])
                if change==0:
                    print(f"Here is your {action} ☕️. Enjoy!")
                else:
                    print(f"You paid {total_money_paid}. The {action} is {cost}. Here is {change} in change.")
                    print(f"Here is your {action} ☕️. Enjoy!")

