import itertools as it
s = "Gokul"
x=0
'''for c in it.cycle(s):
    print(c)
    x+=1
    if x == 30:
        break'''
a = {1:"dhoni",2:"virat",4:"ABD"}
for p in it.permutations(a.values()):
    print(p)
#also can use combinations