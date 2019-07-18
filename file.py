#__a__b match string in sowpods.txt file
fp = open("sowpods.txt")
for line in fp:
    rev = line[::-1]
    #print(rev)
    #print(line)
    '''if (rev == line):
        print("yaaas")
        '''
    ind = 0
    length = len(rev)
    flag = True
    while ind < length:
        if(rev[ind]!=line[ind]):
            print("%s && %s"%(rev[ind],line[ind]))
            flag = False
            break
        ind += 1
    if flag:
        print(rev)
#print("hff")

