# Application to print index 
#of all occurrences of the given substring
s='ABABABABABA'
sub='AB'
i=s.find(sub)
if i==-1:
    print('Substring not available')
while i!=-1:
    print('{} present in index {}'.format(sub,i))
    i=s.find(sub,i+len(sub),len(s))