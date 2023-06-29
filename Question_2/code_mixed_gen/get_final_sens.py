f1 = open('l1','r')
f2 = open('l2','r')
fa = open('pa','r')

f1_f = open('l1_final','a')
f2_f = open('l2_final','a')
fa_f = open('pa_final','a')

L1 = f1.readlines()
L2 = f2.readlines()
LA = fa.readlines()

arr = [1, 20, 26, 31, 32, 34, 38, 64, 66, 69, 85, 87, 90, 110, 112, 115, 124]


for i in arr:
    f1_f.write(L1[i-1])
    f2_f.write(L2[i-1])
    fa_f.write(LA[i-1])