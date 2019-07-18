def decorator(fun,name):
    def wrapper():
        print("before function call")
        fun(name)
        print("after function call")
        return wrapper
@decorator
def print_name(name):
    print("Hello " +name)

#a = decorator(print_name,"Gokul")