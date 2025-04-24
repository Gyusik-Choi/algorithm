package com.example

class NumberOfIslands200_2 {
    private val dy = intArrayOf(-1, 0, 1, 0)
    private val dx = intArrayOf(0, 1, 0, -1)

    fun numIslands(grid: Array<CharArray>): Int {
        var islands = 0
        for (i in grid.indices) {
            for (j in grid[0].indices) {
                if (grid[i][j] == '1') {
                    islands += 1
                    dfs(grid, i, j)
                }
            }
        }
        return islands
    }

    // https://www.baeldung.com/kotlin/void-type
    private fun dfs(grid: Array<CharArray>, y: Int, x: Int): Unit {
        grid[y][x] = '0'

        for (i in 0..3) {
            val yValue = y + dy[i]
            val xValue = x + dx[i]

            when {
                0 > yValue ||
                    yValue >= grid.size ||
                    0 > xValue ||
                    xValue >= grid[0].size ||
                    grid[y][x] == '0' -> continue
                else -> dfs(grid, yValue, xValue)
            }
        }
    }
}
