s=input('Enter the string')
v={'a','e','i','o','u'}
d={}
for ch in s:
    if ch in v:
        d[ch]=d.get(ch,0)+1
print(d)

for k,v in d.items():
    print(k,v)