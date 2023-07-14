#program to check whether the given number is prime or not

num = int(input('Enter the number '))

if num <= 1:
    print('it is not a prime number')
else:
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime == True:
        print('Prime number')
    else:
        print('not prime')
