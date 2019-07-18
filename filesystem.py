import os
class FS(object):
    def __init__(self,root,ext):
        self.root = root
        self.ext = ext
    def list_files(self):
        a = os.walk(self.root)
        for i,j,k in a:
            print(i,j,k)
    def search(self,path,s):
        fp = open(path)
        for lines in fp:
            if lines.find(s)!=-1:
                return True
        return False
    def grep(self,s):
        a = os.walk(self.root)
        for i,j,k in a:
            for files in k:
                if files.endswith(self.ext):
                    #print(files)
                    if self.search(self.root+'/'+files,inp):
                        print("found in " + files)
                    else:
                        print("not found in " + files)



root = input("enter the root directory : ")
ext = input("enter the extension :")
a = FS(root,ext)
inp = input("enter the string to be searched :")
a.grep(inp)