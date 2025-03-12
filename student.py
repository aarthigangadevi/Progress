class Student:


    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = float(gpa)
        self.is_on_probation = is_on_probation


    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

#code for checking if they are on honors
'''from student import Student

student1 = Student("aarthi", "CSE", "3.75", "false")
student2 = Student("aakash", "CSE", "3.75", "false")

print(student2.on_honor_roll())'''
