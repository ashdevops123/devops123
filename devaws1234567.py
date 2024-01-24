from zipfile import *
f=ZipFile("infosys123.zip",'w',ZIP_DEFLATED)
f.write('ashish.txt')
f.write('rajika.txt')
f.write('sagar.txt')
f.close()
print('infosys123.zip is created successfully!!!')


