class student:
    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name

    def fun(self):
        print("My Roll No And Name Is: ", self.rollno, self.name)

s1 = student(1, "abc")
s2 = student(2, "pqr")

s1.fun()
print(s1.rollno, s1.name)
print(s2.rollno, s2.name)
