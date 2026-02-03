package com.example.algorithm

class ThreeSum15_2 {
    fun threeSum(nums: IntArray): List<List<Int>> {
        nums.sort()
        val answer = mutableListOf<List<Int>>()
        for (i in 0 until nums.size - 2) {
            if (i > 0 && nums[i - 1] == nums[i]) {
                continue
            }
            var left = i + 1
            var right = nums.size - 1
            while (left < right) {
                val sums = nums[i] + nums[left] + nums[right]
                if (sums == 0) {
                    answer.add(listOf(nums[i], nums[left], nums[right]))
                    while (left < right && nums[left] == nums[left + 1]) {
                        left += 1
                    }
                    while (left < right && nums[right - 1] == nums[right]) {
                        right -= 1
                    }
                    left += 1
                    right -= 1
                } else if (sums < 0) {
                    left += 1
                } else {
                    right -= 1
                }
            }
        }
        return answer
    }
}
