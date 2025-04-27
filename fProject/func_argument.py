def add(a,b):
    c=a+b
    print(f"sum is {c}")
add(1,5)
add(2,8)

def add(*numbers):
    c=0
    for i in numbers:
        c+=i
    print(f"sum is {c}")
add(4,5)
add(7,8,6,4,8,9)