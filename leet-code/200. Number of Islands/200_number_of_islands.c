static void dfs_recursion(char** grid, const int gridSize, int* gridColSize, const int i, const int j)
{
    if (0 > i || i >= gridSize || 0 > j || j >= gridColSize[i] || grid[i][j] != '1') {
        return;
    }
    grid[i][j] = '0';
    dfs_recursion(grid, gridSize, gridColSize, i - 1, j);
    dfs_recursion(grid, gridSize, gridColSize, i, j + 1);
    dfs_recursion(grid, gridSize, gridColSize, i + 1, j);
    dfs_recursion(grid, gridSize, gridColSize, i, j - 1);
}

int numIslands(char** grid, int gridSize, int* gridColSize)
{
    int cnt = 0;
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridColSize[i]; j++) {
            if (grid[i][j] == '1') {
                cnt += 1;
                dfs_recursion(grid, gridSize, gridColSize, i, j);
            }
        }
    }
    return cnt;
}
