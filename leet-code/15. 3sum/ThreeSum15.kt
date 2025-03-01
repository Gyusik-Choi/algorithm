package com.example.algorithm

import kotlin.collections.ArrayList

class ThreeSum15 {
    fun threeSum(nums: IntArray): List<List<Int>> {
        nums.sort()
        val answer: MutableList<List<Int>> = ArrayList()
        for (i in 0 until nums.size - 2) {
            if (i > 0 && nums[i] == nums[i - 1]) continue
            var left = i + 1
            var right = nums.size - 1
            while (left < right) {
                val sum = nums[i] + nums[left] + nums[right]
                if (sum > 0) {
                    right -= 1
                } else if (sum < 0) {
                    left += 1
                } else {
                    answer.add(listOf(nums[i], nums[left], nums[right]))
                    while (left < right && nums[left] == nums[left + 1]) left += 1
                    while (left < right && nums[right] == nums[right - 1]) right -= 1
                    left += 1
                    right -= 1
                }
            }
        }
        return answer
    }
}