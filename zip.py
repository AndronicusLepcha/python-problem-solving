#module : zipfile
#class : ZipFile

from zipfile import *
f=ZipFile("MyZip.zip",'w',ZIP_DEFLATED)
file1=input("Enter the file name")
file2=input("Enter the file name")
f.write(file1)
f.write(file2)