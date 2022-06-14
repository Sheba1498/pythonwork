lst=[10,14,2,14,14,20]
st=set(lst)
print(st)

st1={1,2,3,4,5}
st2={7,9,10,14,5,4}
union_set=st1.union(st2)
print(union_set)

intersection_set=st1.intersection(st2)
print(intersection_set)

diiference_set=st1.difference(st2)
print(diiference_set)

students=["ram","ravi","hari","tom","nikhil","jain","john"]
passed_students=["ravi","hari","tom"]
st_students=set(students)
st_passed_stu=set(passed_students)
failed_students=st_students.difference(st_passed_stu)

print(failed_students)
