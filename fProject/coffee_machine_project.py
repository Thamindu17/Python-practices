menu={
    "latte":{
        "ingredients":{
            "water":200,
            "milk":140,
            "coffee":50
        },
        "cost":150
    },
    "cappucinno": {
        "ingredients": {
            "water": 200,
            "milk": 120,
            "coffee": 30
        },
        "cost": 200
    },
    "esp": {
        "ingredients": {
            "water": 200,
            "coffee": 60
        },
        "cost": 100
    },



}
money=0
resources={
    "coffee":500,
    "milk":400,
    "water":800

}
def check_ingre(order_ingrediants):
    for item in order_ingrediants:
        if order_ingrediants[item]>resources[item]:
            print(f"sry there are enough {item}")
            return False
    return True
def collect_money():
    print("enter the money")
    total=0
    count_of_twenty_note=int(input("enter count of 20 notes:"))
    count_of_fifty_note = int(input("enter count of 50 notes:"))
    count_of_hundred_note = int(input("enter count of 100 notes:"))
    total=count_of_twenty_note*20+count_of_fifty_note*50+count_of_hundred_note*100
    return total
def is_payment_successful(payment,coffee_cost):
    if payment>=coffee_cost:
        global money #directly can't access global variable
        change=payment-coffee_cost
        print(f"here is your balance {change}.")
        return True
    else:
        print("that's enough,your money refunded.")
        return False

def make_coffee(choice,coffee_ingrediants):
    for item in coffee_ingrediants:
        resources[item]-=coffee_ingrediants[item]
    print(f"here is your {choice} coffee.......")



is_on=True
while is_on:
    choice=input("what would you like to have?(latte/esp/cappucinno):")
    if choice=="off":
        print("bye")
        is_on=False
    elif choice=="report":
        print(f"coffee={resources['coffee']}g")
        print(f"water={resources['water']}ml")
        print(f"milk={resources['milk']}ml")
        print(f"total money:Rs.{money}")
    else:
        coffee_type=menu[choice]
        print(coffee_type)
        if check_ingre(coffee_type['ingredients']):
            payment=collect_money()
            if is_payment_successful(payment,coffee_type['cost']):
                make_coffee(choice,coffee_type['ingredients'])
