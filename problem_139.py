#Find no of occurrences of each 
#character present in given string with count
s=input('enter the string')
s1=set(s)
for ch in s1:
    print('{} occurs {} times'.format(ch,s.count(ch)))