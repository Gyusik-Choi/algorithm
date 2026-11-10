static void traverse(char** map, const int y_length, const int x_length, const int y, const int x) {
    if (0 > y || y >= y_length || 0 > x || x >= x_length) {
        return;
    }
    if (map[y][x] == '0') {
        return;
    }
    map[y][x] = '0';
    traverse(map, y_length, x_length, y - 1, x);
    traverse(map, y_length, x_length, y, x + 1);
    traverse(map, y_length, x_length, y + 1, x);
    traverse(map, y_length, x_length, y, x - 1);
}

int numIslands(char** grid, int gridSize, int* gridColSize) {
    int cnt = 0;
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridColSize[i]; j++) {
            if (grid[i][j] == '1') {
                cnt++;
                traverse(grid, gridSize, gridColSize[i], i, j);
            }
        }
    }
    return cnt;
}