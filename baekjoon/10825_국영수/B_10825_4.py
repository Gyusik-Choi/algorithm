import sys


N = int(sys.stdin.readline())
grades = []

for _ in range(N):
    grade = list(sys.stdin.readline().split())

    grade[1] = int(grade[1])
    grade[2] = int(grade[2])
    grade[3] = int(grade[3])

    grades.append(grade)

grades.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
sys.stdout.write('\n'.join(list(map(lambda x: x[0], grades))))

# map 함수 참고
# https://blockdmask.tistory.com/531
