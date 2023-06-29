import nltk
from nltk.tokenize import RegexpTokenizer

f = open('cms.txt','r')

lines = f.readlines()


def find_cmi(line):
    
    w = 0
    u = 0
    n = len(line.strip().split())
    for word in line.split():
        for char in word:
            if char.isascii() == True:
                if char.isdigit() == True or char == '#' or char == '@':
                    u = u + 1
                    break
            else:
                w = w + 1
                break
    cmi = 100*(1-(w/(n-u)))
    return cmi



    

f1 = open('train','w')
key = 0
for i in range(0,len(lines)):
    ind = find_cmi(lines[i])
    if ind == 100:
        key = i
    f1.write('\n'.join(['\t'.join((lines[key],lines[i]))]))



