import sys


N = int(sys.stdin.readline())
students = []

for _ in range(N):
    name, korean, english, math = sys.stdin.readline().split()
    students.append([name, int(korean), int(english), int(math)])

students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
sys.stdout.write('\n'.join(list(map(lambda x: x[0], students))))
