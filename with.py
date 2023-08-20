with open('with.txt','w') as f:
    data=input('Enter the data to write in the file')
    f.write(data)
    print(f.tell())

print('write completed')
print('is file closed: ',f.closed)