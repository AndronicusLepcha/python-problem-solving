s='AABBCCDDDD'
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
print(d)
out=''
for k,v in d.items():
    out=out+str(v)+k
print(out)