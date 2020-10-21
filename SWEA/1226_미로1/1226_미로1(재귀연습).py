import sys
sys.stdin = open('input.txt', 'r')


def dfs_recursion(go):
    global visited, result
    visited[go[0]][go[1]] = 1
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    for i in range(4):
        ay = go[0] + dy[i]
        ax = go[1] + dx[i]
        if 0 <= ay < 16 and 0 <= ax < 16:
            if arr[ay][ax] == 3 or result:
                result = 1
                return
            if visited[ay][ax] != 1 and arr[ay][ax] == 0 and not result:
                dfs_recursion([ay, ax])
    return


T = 10
for tc in range(1, T+1):
    t = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    start = [1, 1]
    result = 0
    dfs_recursion(start)
    if result:
        print("#{} {}".format(t, 1))
    else:
        print("#{} {}".format(t, 0))
