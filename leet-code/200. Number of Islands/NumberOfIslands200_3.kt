package com.example

import java.util.LinkedList

class NumberOfIslands200_3 {
    private val yIdx = intArrayOf(-1, 0, 1, 0)
    private val xIdx = intArrayOf(0, 1, 0, -1)

    fun numIslands(grid: Array<CharArray>): Int {
        var cnt = 0
        for (i in grid.indices) {
            for (j in grid[0].indices) {
                if (grid[i][j] == '1') {
                    cnt += 1
                    dfsStack(grid, i, j)
                }
            }
        }
        return cnt
    }

    private fun dfsStack(grid: Array<CharArray>, y: Int, x: Int) {
        val stack = LinkedList<IntArray>()
        stack.push(intArrayOf(y, x))
        while (stack.isNotEmpty()) {
            val item = stack.pop()
            grid[item[0]][item[1]] = '0'
            for (i in 0..3) {
                val yValue = item[0] + yIdx[i]
                val xValue = item[1] + xIdx[i]
                if (0 > yValue || yValue >= grid.size || 0 > xValue || xValue >= grid[0].size) {
                    continue
                }
                if (grid[yValue][xValue] == '0') {
                    continue
                }
                stack.push(intArrayOf(yValue, xValue))
            }
        }
    }
}
