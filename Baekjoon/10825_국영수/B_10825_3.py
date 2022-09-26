import sys


N = int(sys.stdin.readline())
grades = []
for _ in range(N):
    grade = list(sys.stdin.readline().split())
    for i in range(1, len(grade)):
        grade[i] = int(grade[i])
    grades.append(grade)

sorted_grades = sorted(grades, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for idx, student in enumerate(sorted_grades):
    sys.stdout.write(student[0] + "\n")
