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


N = int(sys.stdin.readline().rstrip())
x_axis = []
y_axis = []
z_axis = []
for i in range(N):
    x, y, z = map(int, sys.stdin.readline().split())
    x_axis.append([x, i])
    y_axis.append([y, i])
    z_axis.append([z, i])

x_axis.sort()
y_axis.sort()
z_axis.sort()

min_axis = []

for i in range(N - 1):
    min_axis.append([x_axis[i + 1][0] - x_axis[i][0], x_axis[i][1], x_axis[i + 1][1]])
    min_axis.append([y_axis[i + 1][0] - y_axis[i][0], y_axis[i][1], y_axis[i + 1][1]])
    min_axis.append([z_axis[i + 1][0] - z_axis[i][0], z_axis[i][1], z_axis[i + 1][1]])

min_axis.sort()

p = [_ for _ in range(N + 1)]

answer = 0
cnt = 0
for i in range(len(min_axis)):
    value, start, end = min_axis[i]

    if find_set(start) == find_set(end):
        continue

    answer += value
    union(start, end)

    cnt += 1
    if cnt == N - 1:
        break

sys.stdout.write(str(answer))
