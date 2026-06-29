package com.example

class BinarySearch704_2 {
    fun search(nums: IntArray, target: Int): Int {
        var low = 0
        var high = nums.size - 1
        while (low < high) {
            val mid = low + (high - low) / 2
            if (nums[mid] < target) {
                low = mid + 1
            } else {
                high = mid
            }
        }
        return if (nums[low] == target) low else -1
    }
}
