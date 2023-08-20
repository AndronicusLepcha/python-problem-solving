f=open('robot.txt','w')
print("File name:",f.name)
print("File mode: ",f.mode)
print("Is File closed: ",f.closed)
print("Is file readable: ",f.readable())
print("is file writeable: ",f.writable())
f.close()
print("Is File closed: ",f.closed)

#writing into the file

f=open('robot.txt','a')
f.write('Robot\n')
f.write('Andronicus\n')

#writing list into file

l=['andro\n','Lepcha\n','Namchi\n']
f.writelines(l)
print("Writing Completed")