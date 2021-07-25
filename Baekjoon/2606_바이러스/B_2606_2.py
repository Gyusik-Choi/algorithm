import sys


def dfs_recursion(number, visited):
    global answer
    for num in link[number]:
        if num not in visited:
            answer += 1
            visited.append(num)
            dfs_recursion(num, visited)
    return visited


number_of_computer = int(input())
number_of_pair = int(input())
link = {i: [] for i in range(1, number_of_computer + 1)}
for _ in range(number_of_pair):
    start, end = map(int, sys.stdin.readline().split())
    link[start].append(end)
    link[end].append(start)

answer = 0
dfs_recursion(1, [1])
print(answer)
