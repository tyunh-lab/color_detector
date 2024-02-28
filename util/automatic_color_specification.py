import time
print("0\n0\n0")
for i in range(10):
    print("\033[3A"+str(i)+"\n"+str(i)+"\n"+str(i)+"\n",end="")
    time.sleep(1)


'''
\033[nA #n行上に
\033[nB #n行下に
\033[nC #n行右に
\033[nD #n行左に
'''