students = [False] * 31
for _ in range(28):
    students[int(input())] = True

for student in range(1, 31):
    if not students[student]:
        print(student)
