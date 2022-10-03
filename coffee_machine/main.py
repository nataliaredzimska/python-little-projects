# source: https://www.udemy.com/course/100-days-of-code/

from data import MENU, resources
from make_coffee import print_resources, make_a_coffee


print('type "report" - to see how many resources is left.')
print('type "off" - to end the program.')

# machine resources
money_in_machine = 0
water_amount = resources['water']
milk_amount = resources['milk']
coffee_amount = resources['coffee']

while True:
    user_input = input(f'  What would you like? (espresso/latte/cappuccino): ').lower()

    # print report (how many resources is left)
    if user_input == 'report':
        print_resources(water_amount, milk_amount, coffee_amount, money_in_machine)

    elif user_input == 'off':
        print('Goodbye')
        break

    # choose a coffee type
    else:
        coffee_type = user_input

        # print a cost of coffee
        print(f"Cost: ${MENU[coffee_type]['cost']:.2f}")

        # make coffee if possible
        can_make_coffee = make_a_coffee(coffee_type, water_amount, milk_amount, coffee_amount)

        # when coffee has been made change machine resources
        if can_make_coffee:
            money_in_machine += MENU[coffee_type]['cost']
            water_amount -= MENU[coffee_type]['ingredients']['water']
            milk_amount -= MENU[coffee_type]['ingredients']['milk']
            coffee_amount -= MENU[coffee_type]['ingredients']['coffee']

    # if machine out of resources
    if water_amount < 50:
        print('The machine is out of water. Come later.')
        break
    elif milk_amount <= 0:
        print('The machine is out of milk. Come later.')
        break
    elif coffee_amount < 18:
        print('The machine is out of coffee. Come later.')
        break
