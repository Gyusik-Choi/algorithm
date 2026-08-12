package com.example

class MajorityElement169_3 {
    fun majorityElement(nums: IntArray): Int {
        return majorityElement(nums, 0, nums.lastIndex)
    }

    private fun majorityElement(nums: IntArray, left: Int, right: Int): Int {
        if (left == right) return nums[left]
        val mid = left + (right - left) / 2
        val a = majorityElement(nums, left, mid)
        val b = majorityElement(nums, mid + 1, right)
        val countA = nums.slice(IntRange(left, right)).count { it == a }
        return if ((right - left + 1) / 2 < countA) a else b
    }
}
