import numbers

operations = ["+", "-", "*", "/", "^", "%", "#", "$"]


def select_op(choice):
    if choice in operations:
        return operations.index(choice)
    else:
        print("Unrecognized operation")


while True:
    print("Select operation.")
    print("1.Add      : +")
    print("2.Subtract : -")
    print("3.Multiply : *")
    print("4.Divide   : /")
    print("5.Power    : ^")
    print("6.Remainder: %")
    print("7.Terminate: #")
    print("8.Reset    : $")

    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)

    if (select_op(choice) == 6):
        # program ends here
        print("Done. Terminating")
        exit()
    else:
        num1 = (input("Enter first number: "))
        print(num1)
        # if("$" in num1):
        #      exit()
        if ("$" not in num1 and "#" in num1):
            print("Done. Terminating")
            exit()
        else:
            try:
                num1 = float(num1)
            except ValueError:
                # print("Invalid input for second number")
                continue
            num2 = input("Enter second number: ")
            print(num2)

            if ("$" not in num2 and "#" in num2):
                print("Done. Terminating")
                exit()
            else:

                try:
                    num2 = float(num2)
                except ValueError:
                    # print("Invalid input for second number")
                    continue

            if (select_op(choice) == 0):
                answr = float(num1) + float(num2)
            elif (select_op(choice) == 1):
                answr = num1 - num2
            elif (select_op(choice) == 2):
                answr = num1 * num2
            elif (select_op(choice) == 3):
                if (num2 == 0):
                    print("float division by zero")
                    answr = "None"
                else:
                    answr = float(num1) / float(num2)
            elif (select_op(choice) == 4):
                answr = num1 ** num2
            elif (select_op(choice) == 5):
                answr = num1 % num2

            print(num1, choice, num2, "=", answr)
