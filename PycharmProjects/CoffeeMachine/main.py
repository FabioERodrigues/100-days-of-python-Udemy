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
    "Money": 0,
}

# def check_water(menu_water):
#     water = resources['water']
#     water -= menu_water
#     return water
# def check_milk(menu_milk):
#     milk = resources['milk']
#     milk -= menu_milk
#     return milk
#
# def check_coffee(menu_coffee):
#     coffee = resources['coffee']
#     coffee -= menu_coffee
#     return coffee
def take_money(quarters, dimes, nickles, pennies):
    final_total = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    return final_total
def sufficient_ingredients(drink):
    for item in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True
def sufficent_money(user_total, actual_cost):
    if user_total < actual_cost:
        print("Sorry thats not enough money. Money refunded.")
    elif user_total == actual_cost:
        print("Thanks for the order")
        return True
    else:
        change = user_total - actual_cost
        changed = round(change, 2)
        print(f"here is ${changed} dollars in change.")
        return True


running = True
while running:
    response = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if response == "off":
        running = False
    elif response == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['Money']}")
    elif response in MENU:
        if sufficient_ingredients(response):
            print("Insert coins:")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))
            total_money = take_money(quarters, dimes, nickels, pennies)
            if sufficent_money(total_money, MENU[response]["cost"]):
                for item in MENU[response]["ingredients"]:
                    resources[item] -= MENU[response]["ingredients"][item]
                resources['Money'] += MENU[response]["cost"]
                print(f"Here is your {response}. Enjoy!")
    else:
        print("Invalid selection. Please choose espresso, latte, or cappuccino.")



#TODO: 2.Turn off the Coffee Machine by entering “off” to the prompt.




#TODO: 3. "report" gives details on water, milk, coffee and money of how much left





#TODO: 4. Check if there are enough resources




#TODO: 5. ask the user to insert coins if there are enough resouces.



#TODO: 6. Check if user has inserted enough coins




#TODO: 7. Make coffee