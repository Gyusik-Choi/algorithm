package com.example;

public class NumberOfIslands200_4 {
    public int numIslands(char[][] grid) {
        int cnt = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    cnt += 1;
                    dfs(grid, i, j);
                }
            }
        }
        return cnt;
    }

    private void dfs(char[][] grid, int y, int x) {
        if (0 > y || y >= grid.length || 0 > x || x >= grid[0].length || grid[y][x] == '0') {
            return;
        }
        grid[y][x] = '0';
        dfs(grid, y + 1, x);
        dfs(grid, y - 1, x);
        dfs(grid, y, x + 1);
        dfs(grid, y, x - 1);
    }
}
