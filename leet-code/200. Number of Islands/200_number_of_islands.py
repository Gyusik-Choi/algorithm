def num_islands(grid):
    def dfs_recursion(y, x):
        visited[y][x] = True

        for k in range(4):
            y_idx = y + y_value[k]
            x_idx = x + x_value[k]

            if 0 > y_idx or y_idx >= m or 0 > x_idx or x_idx >= n:
                continue

            if visited[y_idx][x_idx]:
                continue

            if grid[y_idx][x_idx] == '0':
                continue

            dfs_recursion(y_idx, x_idx)

    m = len(grid)
    n = len(grid[0])
    y_value = [-1, 0, 1, 0]
    x_value = [0, 1, 0, -1]
    visited = [[False] * n for _ in range(m)]
    cnt = 0

    for i, row in enumerate(grid):
        for j, r in enumerate(row):
            if visited[i][j]:
                continue

            if grid[i][j] == '0':
                continue

            cnt += 1
            dfs_recursion(i, j)

    return cnt


print(num_islands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))

print(num_islands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
