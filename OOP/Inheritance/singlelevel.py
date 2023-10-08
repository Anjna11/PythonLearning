class parent:

    name = "a"

    def fun1(self):
        # self.name = "b"
        print("This function is defined inside the parent class.")
        print(self.name)

class child(parent):
    def fun2(self):
        self.name = "c"
        print("This function is defined inside the child class.")
        print(self.name)

obj = child()
obj.fun1()
obj.fun2()
print(parent.name)