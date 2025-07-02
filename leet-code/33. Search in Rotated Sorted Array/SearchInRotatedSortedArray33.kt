package com.example

class SearchInRotatedSortedArray33 {
    fun search(nums: IntArray, target: Int): Int {
        val pivot = findPivot(nums)
        val direction = findSearchDirection(nums, target, pivot)
        if (direction == 0) {
            return findTarget(nums, target, 0, pivot - 1)
        }
        return findTarget(nums, target, pivot, nums.size - 1)
    }

    private fun findPivot(nums: IntArray): Int {
        var low = 0
        var high = nums.size - 1
        while (low < high) {
            val mid = low + (high - low) / 2
            if (nums[mid] <= nums[high]) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low
    }

    // 0 -> left, 1 -> right
    private fun findSearchDirection(nums: IntArray, target: Int, pivot: Int): Int {
        return when {
            pivot == 0 || (nums[pivot] <= target && target <= nums[nums.size - 1]) -> 1
            else -> 0
        }
    }

    private fun findTarget(nums: IntArray, target: Int, l: Int, h: Int): Int {
        var low = l
        var high = h
        while (low <= high) {
            val mid = low + (high - low) / 2
            if (nums[mid] == target) {
                return mid
            }
            if (nums[mid] > target) {
                high = mid - 1
            } else {
                low = mid + 1
            }
        }
        return -1
    }
}
