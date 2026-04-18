package com.example.algorithm

class Subsets78_2 {
    fun subsets(nums: IntArray): List<List<Int>> {
        return getSubsets(nums, 0, mutableListOf(), mutableListOf())
    }

    private fun getSubsets(nums: IntArray, idx: Int, subsetList: MutableList<List<Int>>, subset: MutableList<Int>): List<List<Int>> {
        subsetList.add(subset.toList())
        if (nums.size == idx) {
            return subsetList
        }
        for (i in idx until nums.size) {
            subset.add(nums[i])
            getSubsets(nums, i + 1, subsetList, subset)
            subset.removeLast()
        }
        return subsetList
    }
}
