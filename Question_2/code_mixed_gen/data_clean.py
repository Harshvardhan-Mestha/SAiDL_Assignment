
f_l1 = open('l1', 'r')
f_l2 = open('l2', 'r')
f_pa = open('pa', 'r')

l_l1 = f_l1.readlines()
l_l2 = f_l2.readlines()
l_pa = f_pa.readlines()

tl = len(l_l2)

f_lang1 = open('hi-to-en-input_lang1', 'a')
f_lang2 = open('hi-to-en-input_lang2', 'a')
f_align = open('hi-to-en-input_parallel_alignments', 'a')

c = 0

for i in range(0,tl):
    if (str(l_l2[i])=='^\n'):
        c = c + 0
    else:
        f_lang1.write(l_l1[i]);#f_lang1.write('\n');
        f_lang2.write(l_l2[i]);#f_lang2.write('\n');
        f_align.write(l_pa[i]);#f_align.write('\n');
        c = c + 1

print(c)





        

