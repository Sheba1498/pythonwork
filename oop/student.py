class student:
    name:str
    rollno:int
    course:str
    def __init__(self,name,rollno,course):
        self.name=name
        self.rollno=rollno
        self.course=course
    def print_student(self):
        print(self.name,self.rollno,self.course)


s1=student("sheba",14,"MSc")
s2=student("Ariya",2,"python")
s1.print_student()
s2.print_student()

