package com.example.algorithm

class SortColors75 {
    fun sortColors(nums: IntArray): Unit {
        var i = 0
        var j = 0
        var k = nums.lastIndex
        while (j <= k) {
            if (nums[j] < 1) {
                swap(nums, i, j)
                i += 1
                j += 1
            } else if (nums[j] > 1) {
                swap(nums, j, k)
                k -= 1
            } else {
                j += 1
            }
        }
    }

    private fun swap(nums: IntArray, idx1: Int, idx2: Int) {
        val temp = nums[idx1]
        nums[idx1] = nums[idx2]
        nums[idx2] = temp
    }
}
