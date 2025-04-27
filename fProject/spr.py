import random
user_input=int(input("enter s for 0,p for 1,r for 2"))
if(user_input>2 or user_input<0):
    print("invalid number")
else:
    computer_choice=random.randint(0,2)
    print(computer_choice)
    if computer_choice==user_input:
        print("draw")
    elif computer_choice==0 and user_input==2:
        print("win")
    elif computer_choice==2 and user_input==0:
        print("lose")
    elif computer_choice>user_input:
        print("lose")
    elif user_input>computer_choice:
        print("win")

