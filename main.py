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
    "money": 0,
}


def report(machine_resources):
    for key in machine_resources:
        if key == "coffee":
            print(f"{key.title()}: {machine_resources[key]}g")
        elif key != "money":
            print(f"{key.title()}: {machine_resources[key]}ml")
        else:
            print(f"{key.title()}: ${round(machine_resources[key], 2)}")


def check_resources(drink_chosed):
    for ingredient in drink_chosed:
        if resources[ingredient] >= drink_chosed[ingredient]:
            return True
        else:
            print(f"Sorry, there is not enough {ingredient}.")
            return False


def deduct_ingredients(drink_chosed):
    for key in drink_chosed:
        resources[key] -= drink_chosed[key]


stop_machine = False

while not stop_machine:
    drink = input("What would you like? (espresso/latte/cappuccino): ")

    if drink == 'report':
        report(resources)
    elif drink == "off":
        stop_machine = True
    else:
        ingredients = MENU[drink]["ingredients"]
        cost = MENU[drink]["cost"]

        if check_resources(ingredients):
            print("Please insert coins.")
            q = int(input("how many quarters? "))
            d = int(input("how many dimes? "))
            n = int(input("how many nickles? "))
            p = int(input("how many pennies? "))
            total_money = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01

            if cost > total_money:
                print("Sorry that's not enough money. Money refunded")
                check_cost = False
            elif cost == total_money:
                resources["money"] = total_money
                check_cost = True
            elif cost < total_money:
                resources["money"] += cost
                change = round(total_money - cost, 2)
                check_cost = True
                print(f"Here is ${change} in change.")

            if check_cost:
                deduct_ingredients(ingredients)
                print(f"Here is your {drink}. \U0001F375 Enjoy!")
