numbers=input("enter numbers list:")
numbers_list=numbers.split()
print(numbers_list)
count=0
for number in numbers_list:
    count+=1
print(f"length of list is {count}")
for i in range(count):
    numbers_list[i]=int(numbers_list[i])
print(numbers_list)
maxnumber=numbers_list[0]
for number in numbers_list:
    if number>maxnumber:
        maxnumber=number
print(f"maximum number is :{maxnumber}")