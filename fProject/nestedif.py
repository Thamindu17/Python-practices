height=int(input("enter height"))
if(height>3):
    print("can")
    age=int(input("input age"))
    if(age>18):
        print("pay 250")
    elif(age>15):
        print("pay 150")
    else:
        print("pay 100")
else:
    print("can't")
print("bye")
