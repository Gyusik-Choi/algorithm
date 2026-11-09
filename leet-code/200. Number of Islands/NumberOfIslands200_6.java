package com.example;

public class NumberOfIslands200_6 {
    public int numIslands(char[][] grid) {
        int cnt = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    cnt += 1;
                    traverse(grid, i, j);
                }
            }
        }
        return cnt;
    }

    private void traverse(char[][] map, int y, int x) {
        if (0 > y || y >= map.length || 0 > x || x >= map[0].length) {
            return;
        }
        if (map[y][x] == '0') {
            return;
        }
        map[y][x] = '0';
        traverse(map, y - 1, x);
        traverse(map, y, x + 1);
        traverse(map, y + 1, x);
        traverse(map, y, x - 1);
    }
}
