package com.example

class MajorityElement169_2 {
    fun majorityElement(nums: IntArray): Int {
        return findMajorityElement(nums, 0, nums.lastIndex)
    }

    private fun findMajorityElement(nums: IntArray, left: Int, right: Int): Int {
        if (left == right) {
            return nums[left]
        }
        val mid = left + (right - left) / 2
        val low = findMajorityElement(nums, left, mid)
        val high = findMajorityElement(nums, mid + 1, right)
        var countLow = 0
        for (i in left..right) {
            if (low == nums[i]) {
                countLow += 1
            }
        }
        if ((right - left + 1) / 2 < countLow) {
            return low
        }
        return high
    }
}
