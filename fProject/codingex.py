student_marks={
    "jeny":99,
    "thamindu":80,
    "kamala":72,
    "amal":65,
    "kamal":40,
    "ajith":20
}
student_grade={}
for student in student_marks:
    marks=student_marks[student]

    if marks>90:
        student_grade[student]="A"
    elif marks>70:
        student_grade[student]="B"
    elif marks>60:
        student_grade[student]="c"
    elif marks>35:
        student_grade[student]="S"
    else:
        student_grade[student]="W"
print(student_grade)