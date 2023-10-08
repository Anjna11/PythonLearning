class demo:
    pass

class Student:
    def __init__(self, n, r):
        self.name = n
        self.rollno = r

    def display(self):
        print("Name And Roll No of Student Is: ", self.name, self.rollno)

a = Student("anjna", 1)
a.display()

a.name = "Disha"
a.display()

# b = demo()
# b.name = "divyesh"
# a.display()