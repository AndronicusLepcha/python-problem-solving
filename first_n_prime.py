#Program to generate first n prime numbers?
num=int(input('Enter the n number'))
count=0
n1=2
while True:
    is_prime=True
    for i in range(2,n1//2+1):
        if n1%2==0:
            is_prime=False
            break
    if is_prime==True:
            print(n1)
            count=count+1
    if count==num:
            break
    n1=n1+1