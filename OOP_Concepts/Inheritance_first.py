class Student:
    def __init__(self, roll, name, gender, age):
        self.roll = roll
        self.name = name
        self.gender = gender
        self.age = age

class Course(Student):
    def __init__(self, roll, name, gender, age, cname, duration, fee):
        super().__init__(roll, name, gender, age)
        self.cname = cname
        self.duration = duration
        self.fee = fee

    def display(self):
        print(self.roll, self.name, self.gender, self.age)
        print(self.cname, self.duration, self.fee)

c = Course(1, "Keyur", "Male", 22, "MCA", "2 Years", 50000)
c.display()