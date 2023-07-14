# list all element divisible by 10 for 1 to 1000
l=[]
for x in range(1,101):
    if x%10 == 0:
        l.append(x)
print(l)
