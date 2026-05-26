
n = int(input())
students = {}

for i in range(n):
    student_name, student_grade = input().split()
    if student_name not in students:
        students[student_name] = []
    students[student_name].append(float(student_grade))

for name, grades in students.items():
    avg = sum(grades) / len(grades)
    print(f"{name} -> {' '.join([f'{el:.2f}' for el in grades])} (avg: {avg:.2f})")


