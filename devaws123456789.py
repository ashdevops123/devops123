from zipfile import *
f=ZipFile('infosys123.zip','r',ZIP_STORED)
names=f.namelist()
#print(names)
for name in names:
    print('The file name',name)
    print('The containts of this file:')
    f1=open(name,'r')
    print(f1.read())
    print()
