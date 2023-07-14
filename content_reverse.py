#Write a Program To REVERSE internal content of each word
s=input('Enter the string')
l=s.split()
#print(l)
l1=[] #empty list to add the revesed word 
for word in l:
    l1.append(word[::-1]) # it will append the word from l, also 
                        #do the reverse of each word
#print(l1)
# we need a complete string so do the join operation
out=' '.join(l1)
print(out)