a = input("enter a string")
b = input("enter another string")
fp = open("sowpods.txt")
x = sorted(b)
length = len(a)
for line in fp:
    if len(line)-1 == length:
        ind = 0
        flag = True
        while ind < length:
            if a[ind]=='_':
                ind += 1
                continue
            elif a[ind]!=line[ind]:
                flag = False
                break
            ind += 1
        y = sorted(line)
        y.pop(0)
        if (flag == True) and (x == y):
            print(line)
fp.close()