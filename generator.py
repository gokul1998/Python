def main():
    for i in inclusive_range(10,25,4,9):
        print(i,end=' ',flush=True)

def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1
    if numargs < 1 :
        raise TypeError(f'expected atleast one arg, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start,stop) = args
    elif numargs == 3:
        (start,stop,step) = args
    elif numargs > 3:
        raise TypeError(f'expected atmost 3 args, got {numargs}')
    
    i = start
    while i <= stop:
        yield i
        i += step




if __name__ == '__main__': main()