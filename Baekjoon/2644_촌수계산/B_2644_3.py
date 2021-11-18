def dfs(t1, t2):
    stack = [t1]

    while stack:
        target = stack.pop()
        if target == t2:
            return

        for person in persons[target]:
            if not visited[person]:
                visited[person] = visited[target] + 1
                stack.append(person)


n = int(input())
target1, target2 = map(int, input().split())
m = int(input())
persons = {i: [] for i in range(n + 1)}

for j in range(m):
    p1, p2 = map(int, input().split())
    persons[p1].append(p2)
    persons[p2].append(p1)

visited = [0] * (n + 1)
dfs(target1, target2)
if not visited[target2]:
    print(-1)
else:
    print(visited[target2])

