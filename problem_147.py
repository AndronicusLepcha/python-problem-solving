s1='abadfd'
s2='asd'
s3='afddggasdf'

out=''
i=j=k=0
while i<len(s1) or j<len(s2) or k<len(s3):
    if i<len(s1):
        out=out+s1[i]
        i=i+1
    if j<len(s2):
        out=out+s2[j]
        j=j+1
    if k<len(s3):
        out=out+s3[k]
        k=k+1
    print(out)