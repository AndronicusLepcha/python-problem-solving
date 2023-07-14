# == and !=

a=90
b=99

print(a==b)
print(a != b)

#chaining of equality operator

print(10 == 10 == 20)
 
# is is ment to compare with the object 
# = is used to check the content

l1=[10,20,30]
l2=[10,20,30]
print(l1 is l2) # false
print(l1==l2) #true
l3=l1
print(l1 is l3) # true