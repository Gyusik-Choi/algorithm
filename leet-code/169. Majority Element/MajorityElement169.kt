package com.example

class MajorityElement169 {
    fun majorityElement(nums: IntArray): Int {
        return findMajority(nums, 0, nums.size - 1)
    }

    private fun findMajority(nums: IntArray, left: Int, right: Int): Int {
        if (left >= right) {
            return nums[left]
        }

        val mid = left + (right - left) / 2
        val m1 = findMajority(nums, left, mid)
        val m2 = findMajority(nums, mid + 1, right)
        var countM1 = 0
        for (i in left..right) {
            if (nums[i] == m1) {
                countM1++
            }
        }
        return if (countM1 > (right - left + 1) / 2) {
            m1
        } else {
            m2
        }
    }
}
