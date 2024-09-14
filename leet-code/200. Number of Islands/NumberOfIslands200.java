public class NumberOfIslands200 {
    public int numIslands(char[][] grid) {
        int y = grid.length;
        int x = grid[0].length;
        boolean[][] visited = new boolean[y][x];
        int cnt = 0;
        for (int i = 0; i < y; i++) {
            for (int j = 0; j < x; j++) {
                if (visited[i][j]) continue;
                if (grid[i][j] == '0') continue;
                cnt += 1;
                visited[i][j] = true;
                dfsRecursive(grid, i, j, visited);
            }
        }
        return cnt;
    }

    private void dfsRecursive(char[][] map, int n, int m, boolean[][] visit) {
        int[] yValue = new int[]{-1, 0, 1, 0};
        int[] xValue = new int[]{0, 1, 0, -1};
        for (int i = 0; i < 4; i++) {
            int yIdx = n + yValue[i];
            int xIdx = m + xValue[i];

            if (yIdx < 0 || yIdx >= visit.length || xIdx < 0 || xIdx >= visit[0].length) continue;
            if (visit[yIdx][xIdx]) continue;
            if (map[yIdx][xIdx] == '0') continue;

            visit[yIdx][xIdx] = true;
            dfsRecursive(map, yIdx, xIdx, visit);
        }
    }
}
