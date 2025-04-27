student_data=[
    {
        "name":"thamindu",
        "roll_no":10,
        "age":20,
        "course":"python"
    },
    {
        "name":"kamal",
        "roll_no":20,
        "age":22,
        "course":"java"
    }

]
def add_newstudent(name,rollno,age,course):
    new_student={}
    new_student["name"]=name
    new_student["roll_no"]=rollno
    new_student["age"]=age
    new_student["course"]=course
    student_data.append(new_student)
add_newstudent("sunil",30,25,"c##")
print(student_data)