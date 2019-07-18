a = int(input("enter a number"))
#list comprehension
b = sum([number**2 for number in list(range(0,a+1,2))])
print(b)
    