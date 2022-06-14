student={"name":"ram","rollno":14,"cls":"plus2","div":"b"}
print(student["name"])
print(student["cls"])
print(student["rollno"])
print(student["div"])

print("subject" in student)
student["subject"]="science"
print(student)

print("school" in student)
student["school"]="GBHSS Chavara"
print(student)

student["rollno"]=36
print(student)

