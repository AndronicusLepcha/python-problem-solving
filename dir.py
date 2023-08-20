import os
cwd=os.getcwd()
print("current working directory is ",cwd)

#make directory
#os.mkdir("Robot")
#os.makedirs("Robot123/cat/dog")
#os.rmdir('Robot')
#os.removedirs('Robot123/cat/dog')
#os.rename('Robot','Hacker')
dir=os.listdir()
for l in dir:
    print(l)
    print()
print("directory created")

s=os.stat('count.py')

#print(s)

os.system('cat add.py')