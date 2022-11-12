
import os, os.path
file = open('./DSPJ/static/files/texttest.txt','w')

file.write('asd ')
file.write('asda ')
file.close

f = open("./DSPJ/static/files/texttest.txt", "r")
article = f.read()
print(article)
