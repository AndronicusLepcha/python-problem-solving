import os
fname=input('Enter the file name')
if os.path.isfile(fname):
    print('File found')
    lcount=wcount=c_count=0
    f=open(fname,'r')
    print(type(f))
    for l in f:
        lcount=lcount+1
        n_word=len(l.split())
        wcount=n_word+wcount
        c_count=c_count+len(l) #character count

    print("Line count is ",lcount)
    print('no of word in line ',wcount)
    print('character count is ',c_count)
else:
    print("file does not exist")
