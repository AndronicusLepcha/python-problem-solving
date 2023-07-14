s1='AAAAAA'
s2='BB'
i,j=0,0
out=''
while i<len(s1) or j<len(s2):
    #out=out+s1[i]+s2[j]
    #i=i+1
    #j=j+1
    if i<len(s1):
        out=out+s1[i]
        i=i+1
    if j<len(s2):
        out=out+s2[j]
        j=j+1
print(out)