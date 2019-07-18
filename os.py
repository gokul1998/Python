import os
def search(f,inp):
    fp = open(f)
    for lines in fp:
        if lines.find(inp)!=-1:
            return True
    return False
#hello    
inp = input("enter a string")
a = os.walk("/Users/gokulakrishnan.parir/Desktop/")
for i,j,k in a:
    for files in k:
        if files.endswith(".txt"):
            #print(files)
            if search("/Users/gokulakrishnan.parir/Desktop/"+files,inp):
                print("found in " + files)
            else:
                print("not found in " + files)
