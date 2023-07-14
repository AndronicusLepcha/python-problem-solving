# Program To REVERSE internal content of every 2nd word present 
#in given string 
s=input('Enter the String')
l=s.split() #it will store the string in list
#print(l)
i=0 # to find every 2nd word present 
l1=[] # creating empty list to store the result
while i<len(l):
    if i%2==0: #check the even index
        l1.append(l[i][::-1])
        #if found then the content will be appended 
        #also the conten will be reversed
    else: # else simply append the string in list
        l1.append(l[i])
    i=i+1 # also need to increment the i or index
#print(l1)
#we need the output in sentence format so to do that use join
out=' '.join(l1) #join the content of l1 with space
print(out)
