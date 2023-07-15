#anonymous function
s=lambda n:n*n
print("square of 10 is",s(10))
x=lambda a,b:a+b
print('addtion of 10 and 30 is',x(10,30))

bigger = lambda a,b: a if a>b else b
print('bigger of 20 and 40 is ',bigger(20,40))