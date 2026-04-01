package com.example;

public class NumberOfIslands200_5 {
    private static final int[] yIdx = new int[]{-1, 0, 1, 0};
    private static final int[] xIdx = new int[]{0, 1, 0, -1};

    public int numIslands(char[][] grid) {
        int cnt = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    cnt += 1;
                    dfsRecursion(grid, i, j);
                }
            }
        }
        return cnt;
    }

    private void dfsRecursion(char[][] map, int y, int x) {
        map[y][x] = '0';
        for (int i = 0; i < 4; i++) {
            int yValue = y + yIdx[i];
            int xValue = x + xIdx[i];
            if (0 > yValue || yValue >= map.length || 0 > xValue || xValue >= map[0].length) {
                continue;
            }
            if (map[yValue][xValue] == '0') {
                continue;
            }
            dfsRecursion(map, yValue, xValue);
        }
    }
}
