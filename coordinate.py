class coordinate(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    def __str__(self):
        return '<' + str(self.getx())+','+str(self.gety())+'>'

a = coordinate(2,3)
b= coordinate(2,4)
print(a==b)
