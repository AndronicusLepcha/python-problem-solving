s='a3n4b6'
out=''
for ch in s:
    if ch.isalpha():
        x=ch
    else: 
        d=int(ch)
        out=out+x*d
print(''.join(sorted(out)))