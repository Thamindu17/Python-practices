import random
letters=['a','b','c','d','e','f','g','h','l']
numbers=['1','2','3','4','5','6','7','9','0']
symbols=['/','>','<','[',']']
n_letters=int(input("letters count: \n" ))
n_numbers=int(input("numbers count:\n" ))
n_symbols=int(input("symbols count:\n" ))
password=""
for i in range(0,n_letters):
    char=random.choice(letters)
    password=password+char
for i in range(0,n_numbers):
    char=random.choice(numbers)
    password=password+char
for i in range(0,n_symbols):
    char=random.choice(symbols)
    password=password+char

print(password)

password_list=[]
for i in range(0,n_letters):
    char=random.choice(letters)
    password_list+=char
for i in range(0,n_numbers):
    char=random.choice(numbers)
    password_list+=char
for i in range(0,n_symbols):
    char=random.choice(symbols)
    password_list+=char

print(password_list)
random.shuffle(password_list)
print(password_list)

password=""
for i in password_list:
    password+=i

print(password)