def check_trip_possible(s, e):
    if find_set(s) == find_set(e):
        return True
    return False


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


N = int(input())
M = int(input())

cities = []
for i in range(N):
    link = list(map(int, input().split()))
    cities.append(link)

travel_plan = list(map(int, input().split()))

p = [0] * (N + 1)
for j in range(1, N + 1):
    make_set(j)

for k in range(len(cities)):
    for l in range(len(cities[k])):
        linked = cities[k][l]
        if linked:
            union(k + 1, l + 1)

flag = True
for m in range(1, len(travel_plan)):
    start = travel_plan[m - 1]
    end = travel_plan[m]
    result = check_trip_possible(start, end)
    if not result:
        print("NO")
        flag = False
        break

if flag:
    print("YES")
