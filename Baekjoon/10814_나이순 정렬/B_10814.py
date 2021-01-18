import sys


N = int(input())
arr = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    arr.append([age, name])

arr.sort(key=lambda x: int(x[0]))
for person in arr:
    sys.stdout.write(' '.join(person) + '\n')
