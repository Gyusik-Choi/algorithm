package com.example

class IntersectionOfTwoArrays349_3 {
    fun intersection(nums1: IntArray, nums2: IntArray): IntArray {
        nums1.sort()
        val result: MutableSet<Int> = hashSetOf()
        for (num in nums2) if (containsNum(nums1, num)) result.add(num)
        return result.toIntArray()
    }

    private fun containsNum(nums: IntArray, target: Int): Boolean {
        var left = 0
        var right = nums.size - 1
        while (left <= right) {
            val mid = left + (right - left) / 2
            if (nums[mid] == target) return true
            if (nums[mid] < target) left = mid + 1
            else right = mid - 1
        }
        return false
    }
}