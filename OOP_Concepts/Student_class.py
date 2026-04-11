class Student:
    def AddStudent(self):
        self.roll = input("Enter Roll No: ")
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.gender = input("Enter Gender: ")

    def DisplayStudent(self):
        print("Roll:", self.roll)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)

s = Student()
s.AddStudent()
s.DisplayStudent()