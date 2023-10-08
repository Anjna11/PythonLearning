class Parent:
    def fun1(self):
        print("This function is defined inside the parent class.")

class Son(Parent):
    def fun2(self):
        print("This function is defined inside the Son class.")

class Dougher(Parent):
    def fun3(self):
        print("This function is defined inside the Dougher class.")

s = Son()
d = Dougher()

s.fun1()
s.fun2()

d.fun1()
d.fun3()