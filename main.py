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

money = 0


def compare_resources(drink, MENU, resources, money):
    for k in resources:
        if MENU[drink]["ingredients"][f"{k}"] > resources[f"{k}"]:
            print(f"Sorry there is not enough {k}.")
            return money
    return payment(drink, MENU, money, resources)

def reduce_resources(drink,MENU, resources):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]

def payment(drink, MENU, money, resources):
    print(f"For {drink} insert ${MENU[drink]["cost"]}.")
    quarters = int(input(f"How many quarters?: "))
    dimes = int(input(f"How many dimes?: "))
    nickles = int(input(f"How many nickles?: "))
    pennies = int(input(f"How many pennies?: "))

    quarters *= 0.25
    dimes *= 0.10
    nickles *= 0.05
    pennies *= 0.01

    sum = round(quarters,2) + round(dimes,2) + round(nickles,2) + round(pennies,2)
    rest = sum - MENU[drink]["cost"]

    if rest > 0:
        print(f"Here is ${round(rest, 2)} in change.")

    if rest >= 0:
        money += MENU[drink]["cost"]
        reduce_resources(drink, MENU, resources)
        print(f"Here is you {drink} ☕ Enjoy!")
    else:
        print("“Sorry that's not enough money. Money refunded.")
    return money


while resources["water"] >= 50:
    drink = input("What would you like? (espresso/latte/cappuccino): \n").lower()

    if drink == "off":
        break

    elif drink == "report":
        for k in resources:
            if k == "coffee":
                ml_or_g = "g"
            else:
                ml_or_g = "ml"
            print(f"{k}: {resources[k]}{ml_or_g}")
        print(f"Money: ${money}")
        continue
    elif drink in ["espresso", "latte", "cappuccino"]:
        money = compare_resources(drink, MENU, resources, money)
    else:
        print("Invalid")

print("Out of service. Thank You!")