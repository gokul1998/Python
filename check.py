a = input()
b = input()
if type(a) == str or type(b) == str:
    print("string involved")
elif a>b:
    print("bigger")
elif a<b:
    print("smaller")
else:
    print("equal")
