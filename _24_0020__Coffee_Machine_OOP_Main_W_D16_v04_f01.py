#Program Requirements:

# 1. Print report
# 2. Check if the resources are sufficient
# 3. Process the math of the coin
# 4. Check to see if the money transaction was successful
# 5. Make coffee.

from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

#Create Objects from these Blueprint Classes:
#Ex: car = CarBlueprint()
#    object = Class() blueprint

#How to use the Objects, and to call the Methods, and the logic required to put everything together:
# Ex: car.speed
#     Object.Attribute
#     car.stop()
#     Object.Method()

# defining objects by their Class blueprint:
menu = Menu()
# menu_item = MenuItem()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_is_on = True

def start_up_the_coffee_machine():
    global machine_is_on
    while machine_is_on:
        print("Hello, Welcome to Drinky Smort!\n")
        print("Available drinks:", menu.get_items())

        user_drink_selection = input(
            f"What would you like to order, from the above selection? (Type the drink name, 'off' to shutdown, or 'REPORT' for updated inventory and profit reports): ").lower()

        #Generating report if typed "report":
        if user_drink_selection == "report":
            coffee_maker.report()    #print function NOT wanted here, cuz it prints None out too
            money_machine.report()   #print function NOT wanted here, cuz it prints None out too
        elif user_drink_selection == "off":
            print("Goodbye human...")
            machine_is_on = False
        #check inventory levels of selected drink:
        else:
            drink = menu.find_drink(user_drink_selection)
            if drink:
                if coffee_maker.is_resource_sufficient(drink):
                    cost = drink.cost
                    if money_machine.make_payment(cost):
                        coffee_maker.make_coffee(drink)

#run the dang machine
start_up_the_coffee_machine()