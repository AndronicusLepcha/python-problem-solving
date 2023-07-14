s='aaaabbbbc'
i=1
previous=s[0]
c=1
out=''
while i<len(s):
    if s[i]==previous:
        c=c+1
    else:
        out=out+str(c)+previous
        previous=s[i]
        c=1
   
    if i==len(s)-1:
        out=out+str(c)+previous
    i=i+1
print(out)