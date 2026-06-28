package com.example

class SortColors75_2 {
    fun sortColors(nums: IntArray): Unit {
        var i = 0
        var j = 0
        var k = nums.size - 1
        while (j <= k) {
            if (nums[j] < 1) {
                swap(nums, i, j)
                i++
                j++
            } else if (nums[j] > 1) {
                swap(nums, j, k)
                k--
            } else {
                j++
            }
        }
    }

    private fun swap(nums: IntArray, idx1: Int, idx2: Int) {
        val temp = nums[idx1]
        nums[idx1] = nums[idx2]
        nums[idx2] = temp
    }
}
