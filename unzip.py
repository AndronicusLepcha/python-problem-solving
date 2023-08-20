#module : zipfile
#class : ZipFile

from zipfile import *
f=ZipFile("MyZip.zip",'r',ZIP_STORED)
name=f.namelist()
print(name)