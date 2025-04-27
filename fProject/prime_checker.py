def prime_checker(number):
    is_prime=True
    if number==1:
        is_prime=False
    for i in range(2,number):
        if number%i==0:
            is_prime=False
    if is_prime:
        print(f"{number}prime number")
    else:
        print(f"{number} not prime number")


n=int(input("enter number:"))
prime_checker(n)
