number_of_students = int(input())
students = {}

for _ in range(number_of_students):
    line = tuple(input().split())
    student, grade = line
    if student not in students:
        students[student] = []
    students[student].append(float(grade))

for student in students:
    grades = students[student]
    average_grade = sum(grades) / len(grades)
    # Format the grades as a string
    grades_str = ' '.join(map(str, grades))
    # Print the result
    print(f'{student} -> {grades_str} (avg: {average_grade})')