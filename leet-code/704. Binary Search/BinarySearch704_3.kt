package com.example

class BinarySearch704_3 {
    fun search(nums: IntArray, target: Int): Int {
        var low = 0
        var high = nums.size - 1
        while (low <= high) {
            val mid = low + (high - low) / 2
            when {
                nums[mid] < target -> low = mid + 1
                nums[mid] > target -> high = mid - 1
                else -> return mid
            }
        }
        return -1
    }
}
