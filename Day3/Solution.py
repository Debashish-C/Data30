students = {
    "dev": 85,
    "shiv": 92,
    "sema": 78,
    "lala ": 90
}

top_student = max(students, key=students.get)

print("The top student is:", top_student, "with marks:", students[top_student])
