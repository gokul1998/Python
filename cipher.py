a = input("enter the string")
b = int(input("enter a number"))
l = [chr(n) for n in range(97,123)]
for char in a:
    print(l[(l.index(char)+b)%26])
