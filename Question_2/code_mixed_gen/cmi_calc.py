import nltk
from nltk.tokenize import RegexpTokenizer

f = open('cm.txt','r')

lines = f.readlines()

l50 = open('cmi_less_than_50.txt','a')
m50 = open('cmi_more_than_50.txt','a')


for l in lines[1:]:
    w = 0
    u = 0
    n = len(l.split())
    for word in l.split():
        for char in word:
            if char.isascii() == True:
                if char.isdigit() == True or char == '#' or char == '@':
                    u = u + 1
                    break
            else:
                w = w + 1
                break
    cmi = 100*(1-(w/(n-u)))
    print(cmi)
    if(cmi>=50):
        m50.write(str(str(lines[0].strip())+"    "+str(l.strip())+"\n"))
    else:
        l50.write(str(str(lines[0].strip())+"    "+str(l.strip())+"\n"))

l50.close()
m50.close()
    

f1 = open('cm_all.txt','w')

for l in lines:
    f1.write(str(lines[0].strip())+"\t"+str(l.strip())+"\n")




