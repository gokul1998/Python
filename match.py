#__a__b match string in sowpods.txt file
a = input("enter a string")
fp = open("sowpods.txt")
length = len(a)
for line in fp:
    #print(len(line))
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
        if flag == True:
            print(line)
fp.close()



