#Write a Program To REVERSE 
#order of words present in the given string
s=input('Enter the String')
l=s.split() # default it will split based on space
l1=l[::-1] #using the concept of slice operator to reverse the string
#print(l1) #it will print the list 
# we need a comple order string so use the join
out=' '.join(l1) # it will join the list with spaces
print(out)