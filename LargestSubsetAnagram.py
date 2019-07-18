from collections import Counter
arr = [s for s in input("enter strings : ").split()]
#print(sorted(arr))
a = list(sorted(arr))
b = Counter(a)
print(b.most_common(2))
