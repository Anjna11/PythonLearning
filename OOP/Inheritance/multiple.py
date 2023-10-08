class Mother:
    mname = ""

class Father:
    fname = ""

class child(Mother, Father):
    def __init__(self, n):
        self.name = n

    def parents(self):
        print("My Name Is: ", self.name)
        print("My Mother Is: ", self.mname)
        print("My Father Is: ", self.fname)


c = child("Anjna")
c.mname = "Rashila Ben"
c.fname = "Devshi Bhai"
c.parents()