import math
import sys


def union(x, y):
    px = find_set(x)
    py = find_set(y)

    p[py] = px


def find_set(x):
    if p[x] == x:
        return x
    p[x] = find_set(p[x])
    return p[x]


def make_set(x):
    p[x] = x


def get_distance(a, b):
    y1, x1 = a
    y2, x2 = b

    distance = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
    return distance


n = int(sys.stdin.readline().rstrip())
arr = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]

new_arr = []
for i in range(n - 1):
    for j in range(i + 1, n):
        dist = get_distance(arr[i], arr[j])
        new_arr.append([dist, i, j])

p = [0] * (n + 1)
for i in range(n + 1):
    make_set(i)
new_arr.sort()

sums = 0
cnt = 0
for i in range(len(new_arr)):
    d, a, b = new_arr[i]
    if find_set(a) == find_set(b):
        continue

    sums += d
    union(a, b)

    cnt += 1
    if cnt == len(new_arr) - 1:
        break

sys.stdout.write(str(sums))

# 정수가 아닌 소수 좌표들을 어떻게 처리할 것인지
# 소수를 어떻게 인덱스화 해야 할지
# => 입력받은 순서를 인덱스화
# 거리, 출발점, 도착점
