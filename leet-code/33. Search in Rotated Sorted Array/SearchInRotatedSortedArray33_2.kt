package com.example

class SearchInRotatedSortedArray33_2 {
    fun search(nums: IntArray, target: Int): Int {
        val pivot = getMinIdx(nums)
        var left = 0
        var right = nums.lastIndex
        while (left <= right) {
            val mid = left + (right - left) / 2
            val midPivot = (pivot + mid) % nums.size
            when {
                nums[midPivot] < target -> left = mid + 1
                nums[midPivot] > target -> right = mid - 1
                else -> return midPivot
            }
        }
        return -1
    }

    private fun getMinIdx(nums: IntArray): Int {
        var left = 0
        var right = nums.lastIndex
        while (left < right) {
            val mid = left + (right - left) / 2
            if (nums[mid] <= nums[right]) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return left
    }
}
