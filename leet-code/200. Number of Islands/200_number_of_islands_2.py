def num_islands(grid):
    def dfs_recursion(y, x):
        if 0 > y or y >= m or 0 > x or x >= n:
            return

        if grid[y][x] == '0':
            return

        grid[y][x] = '0'

        dfs_recursion(y + 1, x)
        dfs_recursion(y - 1, x)
        dfs_recursion(y, x + 1)
        dfs_recursion(y, x - 1)

    m = len(grid)
    n = len(grid[0])
    cnt = 0

    for i, row in enumerate(grid):
        for j, r in enumerate(row):
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
