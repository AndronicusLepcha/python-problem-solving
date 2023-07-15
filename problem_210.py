#find the factorial
def factorial(num):
    result=1
    while num>=1:
        result=result*num
        num=num-1
    return result
ans=factorial(4)
print("factorial of {} is {}".format(4,ans))