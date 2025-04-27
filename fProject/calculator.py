import os
def add(a,b):
    c=a+b
    return c
def subtract(a,b):
    c=a-b
    return c
def multiply(a,b):
    c=a*b
    return c
def devide(a,b):
    c=a/b
    return c
symbol_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":devide
}
def calculator():

        number1 =float(input("enter number 1:"))
        continue_cal = True
        while continue_cal:
            for i in symbol_dict:
                print(i)
            op_symbol = input("select operator:")
            number2 = float(input("enter number 2:"))
            calculate_function = symbol_dict[op_symbol]
            c = calculate_function(number1, number2)
            print(f"{number1} {op_symbol} {number2}=  {c}")
            next_step = input(f"press 'c' to continue calculation with value {c},for new calculation press 'n', for exit press 'x':").lower()
            if next_step == 'c':
                number1 = c
            elif next_step == 'n':
                continue_cal = False
                os.system('cls')
                calculator()
            elif next_step == 'x':
                continue_cal = False
                print("bye")

calculator()








