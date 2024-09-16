public class NumberOfIslands200_2 {
    public int numIslands(char[][] grid) {
        // NumberOfIslands200 풀이와 달리
        // 별도의 방문 배열을 사용하지 않는다
        // yValue, xValue 와 같은 4방향의 값을 나타내는 별도의 배열을 사용하지 않는다
        int cnt = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    cnt += 1;
                    dfsRecursive(grid, i, j);
                }
            }
        }
        return cnt;
    }

    private void dfsRecursive(char[][] grid, int y, int x) {
        if (y < 0 || y >= grid.length || x < 0 || x >= grid[0].length) return;
        if (grid[y][x] == '0') return;
        grid[y][x] = '0';
        dfsRecursive(grid, y - 1, x);
        dfsRecursive(grid, y, x + 1);
        dfsRecursive(grid, y + 1, x);
        dfsRecursive(grid, y, x - 1);
    }
}
