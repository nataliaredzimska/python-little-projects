from data import MENU


# printing a report
def print_resources(water_machine, milk_machine, coffee_machine, money):
    print(f'Water: {water_machine}ml')
    print(f'Milk: {milk_machine}ml')
    print(f'Coffee: {coffee_machine}g')
    print(f'Money: ${money:.2f}')


# checking machine resources
def check_resources(coffee, water_machine, milk_machine, coffee_machine):
    coffee_to_make = MENU[coffee]
    need_water = coffee_to_make['ingredients']['water']
    need_milk = coffee_to_make['ingredients']['milk']
    need_coffee = coffee_to_make['ingredients']['coffee']

    if not water_machine >= need_water:
        print(' Sorry there is not enough water.')
        return False
    elif not milk_machine >= need_milk:
        print(' Sorry there is not enough milk.')
        return False
    elif not coffee_machine >= need_coffee:
        print(' Sorry there is not enough coffee.')
        return False
    else:
        return True


# checking if customer has enough money
def pay_for_coffee(coffee):
    print('Please insert coins.')

    coffee_cost = MENU[coffee]['cost']

    quarters = int(input('how many quarters?: ')) * 0.25
    dimes = int(input('how many dimes?: ')) * 0.10
    nickles = int(input('how many nickles?: ')) * 0.05
    pennies = int(input('how many pennies?:')) * 0.01

    total = quarters + dimes + nickles + pennies
    if total >= coffee_cost:
        # calculate a change
        if total > coffee_cost:
            change = round(total - coffee_cost, 2)
            print(f'Here is ${change:.2f} in change.')
        return True

    else:
        print("Sorry that's not enough money. Money refunded.")


# making a coffee
def make_a_coffee(coffee, water_machine, milk_machine, coffee_machine):
    # check if machine has enough resources
    can_make = check_resources(coffee, water_machine, milk_machine, coffee_machine)
    if not can_make:
        return False

    # check if customer inserted enough money
    enough_money = pay_for_coffee(coffee)
    if not enough_money:
        return False

    # if everything ok - make coffee
    if can_make and enough_money:
        print(f'Here\'s your {coffee} ☕️. Enjoy!')
        return True
