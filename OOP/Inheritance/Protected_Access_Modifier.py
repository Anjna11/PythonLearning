class Parent:

    _fathername = ""
    _sirname = ""

class Child(Parent):
    def __init__(self, n, fn, sr):
        self.name = n
        self._fathername = fn
        self._sirname = sr

    def display(self):
        print("My Name Is: ", self.name, self._fathername, self._sirname)

a = Child("Disha", "DevshiBhai", "Jagatiya")
a.display()

a._fathername = "Divyesh"
a.display()