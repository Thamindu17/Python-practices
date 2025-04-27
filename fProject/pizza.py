size=input("what size pizza do you want? s/m/l")
bill=0
if size=='s' or size=='S':
    bill+=100
    print("small pizza price is 100")
elif size=='m' or size=='M':
    bill+=200
    print("medium pizza is 200")
else:
    bill+=300
    print("large pizza is 300")
add_pep=input("do you want peperoni?y or n")
if add_pep=='y' or add_pep=='Y':
    if size == 's' or size == 'S':
        bill += 30
    else:
        bill +=50
add_cheese=input("do you want cheese?y/n")
if add_cheese=='y' or add_cheese=='Y':
    bill +=20
print(f"your bill is {bill}")




