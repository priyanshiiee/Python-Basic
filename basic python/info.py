student = {}
def add_student(s_id,name,marks):
    student[s_id]={"name":name, "marks":marks}
    print(f"student {name } added ")
add_student("s_001","priyanshi",91)
print(student)
add_student("s_002","priya",91)
print(student)
