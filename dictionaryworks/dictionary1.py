student={"name":"Sheba","rollno":14,"cls":"MSc","div":"b"}
# print(student["name"])
# print(student["cls"])
# print(student["rollno"])
# print(student["div"])

# print("subject" in student)
# student["subject"]="science"
# print(student)
#
# print("school" in student)
# student["school"]="GBHSS Chavara"
# print(student)
#
# student["rollno"]=36
# print(student)
#
# print(student.get("name"))
# print(student.get("rollno"))
#
# if "faculty" in student:
#     student["faculty"]="John"
# else:
#     student["faculty"]="Hubert"
# print(student)
#
# student["faculty"]="John" if "faculty" in student else "Hubert"
# print(student)



if student["rollno"]>40:
    student["rollno"]+=5
else:
    student["rollno"]-=2
print(student)


