import sys


T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    grades = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    changed_grades = []
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        changed_grades.append([a, b])
    print(changed_grades)

# 위상 정렬
