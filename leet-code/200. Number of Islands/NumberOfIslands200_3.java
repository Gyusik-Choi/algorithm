package com.example;

public class NumberOfIslands200_3 {

    private final int[] dy = new int[]{-1, 0, 1, 0};
    private final int[] dx = new int[]{0, 1, 0, -1};

    public int numIslands(char[][] grid) {
        int islands = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    islands += 1;
                    dfs(grid, i, j);
                }
            }
        }
        return islands;
    }

    private void dfs(char[][] grid, int y, int x) {
        grid[y][x] = '0';

        for (int i = 0; i < 4; i++) {
            int yVal = y + dy[i];
            int xVal = x + dx[i];

            if (0 > yVal || yVal >= grid.length || 0 > xVal || xVal >= grid[0].length) {
                continue;
            }

            if (grid[yVal][xVal] == '0') {
                continue;
            }

            dfs(grid, yVal, xVal);
        }
    }
}
