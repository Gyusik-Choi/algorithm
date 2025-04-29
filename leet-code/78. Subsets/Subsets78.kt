package com.example

class Subsets78 {
    fun subsets(nums: IntArray): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        val subset = mutableListOf<Int>()

        fun dfs(idx: Int) {
            result.add(subset.toList())
            for (i in idx..nums.size - 1) {
                subset.add(nums[i])
                dfs(i + 1)
                subset.removeLast()
            }
        }

        dfs(0)
        return result
    }
}
