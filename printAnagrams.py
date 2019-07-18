n = input("enter n :")
arr = [s for s in input().split()]
dic = {}
for s in arr:
    dic[s] = sorted(s)
print(dic)
print(sorted(dic.items(),key = lambda kv:(kv[1],kv[0])))