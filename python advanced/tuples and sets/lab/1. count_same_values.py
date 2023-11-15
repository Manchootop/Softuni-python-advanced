count = int(input())
students = {}
for _ in range(count):
    line = tuple(input().split())
    student, grade = line
    if student not in students:
        students[student] = []
    students[student].append(float(grade))

[print(student) for student in students]

