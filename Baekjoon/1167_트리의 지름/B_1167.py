import sys
sys.setrecursionlimit(10**9)
import copy


def get_max_idx(arr):
    max_idx = 0
    max_dist = 0
    for m in range(1, len(arr)):
        if arr[m] > max_dist:
            max_dist = arr[m]
            max_idx = m

    return [max_idx, max_dist]


def dfs_recursion(go, v, d):
    v[go] = True
    for end, value in edges[go]:
        if not v[end]:
            d[end] = d[go] + value
            dfs_recursion(end, v, d)

    return d


V = int(sys.stdin.readline().rstrip())
edges = {i: [] for i in range(1, V + 1)}
for _ in range(V):
    edge = list(map(int, sys.stdin.readline().split()))
    for k in range(1, len(edge) - 1, 2):
        edges[edge[0]].append([edge[k], edge[k + 1]])

# 임의의 시작점
start = 1
visited = [False] * (V + 1)
distances = [0] * (V + 1)

first_dfs = dfs_recursion(start, copy.deepcopy(visited), copy.deepcopy(distances))
max_info_first = get_max_idx(first_dfs)

second_dfs = dfs_recursion(max_info_first[0], copy.deepcopy(visited), copy.deepcopy(distances))
max_info_second = get_max_idx(second_dfs)

print(max_info_second[1])
