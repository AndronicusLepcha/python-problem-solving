s='B4A1D3'
print(sorted(s))

alpha=[]
digits=[]

for ch in s:
    if ch.isalpha():
        alpha.append(ch)
    else:
        digits.append(ch)
out=' '.join(sorted(alpha)+sorted(digits))
print(out)