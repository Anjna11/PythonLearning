class Grandfather:
        
    def __init__(self, gfn):
        self.grandfathername = gfn

class Father(Grandfather):
    def __init__(self, fn, gfn):
        self.fathername = fn
        Grandfather.__init__(self, gfn)

class Son(Father):
    def __init__(self, n, fn, gfn):
        self.name = n
        Father.__init__(self, fn, gfn)

    def fun(self):
        print("MY Grandfather Name is: ", self.grandfathername)
        print("MY Father Name is: ", self.fathername)
        print("MY Name is: ", self.name)

a = Son("Divyesh", "Devshibhai", "RamjiBhai")
print(a.grandfathername)  
a.fun()
