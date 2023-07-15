#filter function
l=[0,1,2,3,4,5,6,7,8]
def isEven(n):
    if n%2==0:
        return True
    else:
        return False
l1=list(filter(isEven,l))
print(l1)

#using lamda function
l2=list(filter(lambda n:n%2==0,l))
print(l2)