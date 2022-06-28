class Course:
    course_name:str
    active_status:bool
    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.active_status=kwargs.get("active_status")

    def __str__(self):
        return self.course_name


django=Course()
django.add_course(course_name="django",active_status=True)

bigdata=Course()
bigdata.add_course(course_name="bigdata",active_status=True)
print(django)
print(bigdata)


class Batch:
    course:Course
    batch_code:str
    start_date:str
    def add_batch(self,**kwargs):
        self.course=kwargs.get("course")
        self.batch_code=kwargs.get("batch_code")
        self.start_date=kwargs.get("start_date")
    def __str__(self):
        return self.batch_code

db1=Batch()
db1.add_batch(course=django,batch_code="djmay2k22",start_date="18-05-2022")
bd1=Batch()
bd1.add_batch(course=bigdata,batch_code="bdmay2k22",start_date="18-05-2022")
print(db1)
print(bd1)


class Student:
    student_name:str
    gender:str
    roll_no:str
    batch:Batch
    def add_student(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.gender=kwargs.get("gender")
        self.roll_no=kwargs.get("roll_no")
        self.batch=kwargs.get("batch")
    def __str__(self):
        return self.student_name

rahul=Student()
rahul.add_student(student_name="rahul",gender="male",roll_no="1234",batch=db1)
sheba=Student()
sheba.add_student(student_name="sheba",gender="female",roll_no="1244",batch=db1)
dona=Student()
dona.add_student(student_name="dona",gender="female",roll_no="1233",batch=bd1)
joel=Student()
joel.add_student(student_name="joel",gender="male",roll_no="1245",batch=bd1)
print(joel.batch.course.course_name)
print(dona.batch.course.course_name)
print(sheba.batch.course)