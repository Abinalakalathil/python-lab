
class Student:

    def __init__(self, name, branch, mark):
        self.name = name
        self.branch = branch
        self.mark = mark

    def displayStudent(self):
         print("Name is " + self.name, "Branch is " + self.branch, "Mark is " + self.mark)

    def __del__(self):
        print('Destructor called, Employee deleted.')

stud1 = Student("Abin,", "mca,", "80")
stud2 = Student("Albin,", "mca,", "60")
stud1.displayStudent()
stud2.displayStudent()