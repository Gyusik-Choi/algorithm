def dfs_recursion(t1, t2):
    for person in persons[t1]:
        if visited[person] == -1:
            visited[person] = visited[t1] + 1
            dfs_recursion(person, t2)


n = int(input())
target1, target2 = map(int, input().split())
m = int(input())
persons = {i: [] for i in range(n + 1)}

for j in range(m):
    p1, p2 = map(int, input().split())
    persons[p1].append(p2)
    persons[p2].append(p1)

visited = [-1] * (n + 1)
visited[target1] = 0
dfs_recursion(target1, target2)
print(visited[target2])

