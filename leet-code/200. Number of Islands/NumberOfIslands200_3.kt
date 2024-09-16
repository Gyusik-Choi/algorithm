class NumberOfIslands200_3 {
    fun numIslands(grid: Array<CharArray>): Int {
        fun dfsRecursive(y: Int, x: Int) {
            when {
                (y < 0) ||
                (y >= grid.size) ||
                (x < 0) ||
                (x >= grid[0].size) ||
                (grid[y][x] == '0') -> return
            }
            grid[y][x] = '0'
            dfsRecursive(y - 1, x)
            dfsRecursive(y, x + 1)
            dfsRecursive(y + 1, x)
            dfsRecursive(y, x - 1)
        }

        var cnt = 0
        for (i in grid.indices) {
            for (j in grid[0].indices) {
                if (grid[i][j] == '1') {
                    cnt += 1
                    dfsRecursive(i, j)
                }
            }
        }
        return cnt
    }
}
