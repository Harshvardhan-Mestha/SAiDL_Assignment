import nltk
from nltk.tokenize import RegexpTokenizer

f = open('cms.txt','r')

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
        m50.write(str(l.strip())+"\n")
    else:
        l50.write(str(l.strip())+"\n")

l50.close()
m50.close()
    
# f1 = open('train','w')
# key = 0
# for i in range(0,len(lines)):
#     ind = find_cmi(lines[i])
#     if ind == 100:
#         key = i
#     f1.write(str(lines[key].strip())+"\t"+str(lines[i].strip())+"\n")




