class queue:
    def __init__(self):
        self.a = []
    def insert(self,val):
        self.a.append(val)
    def remove(self):
        b = self.a
        if len(b) == 0:
            print("queue empty")
        else:
            self.a.pop(0)
    def print(self):
        print(self.a)
q = queue()
q.insert(5)
q.insert(4)
q.print()
q.remove()
q.print()
q.remove()
q.remove()
