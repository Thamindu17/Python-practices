name1=input("enter your name?")
name2=input("enter her/his name?")
combined_name=name1+name2
lower_name=combined_name.lower()

t=lower_name.count('t')
r=lower_name.count('r')
u=lower_name.count('u')
e=lower_name.count('e')

true=t+r+u+e

l=lower_name.count('l')
o=lower_name.count('o')
v=lower_name.count('v')
e=lower_name.count('e')

love=l+o+v+e

lovescore=int(str(true)+str(love))

if lovescore<10 or lovescore>90:
    print(f"Your score is {lovescore} and you go together like mentoes and coke")
elif lovescore>=40 and lovescore<=50:
    print(f"your score is {lovescore} and u alright")
else:
    print(f"u love is {lovescore}")

