package com.example

import kotlin.math.max

class HouseRobber198_2 {
    fun rob(nums: IntArray): Int {
        // dp
        // 직전의 값을 그대로 올리거나
        // 직전 이전의 값과 더하거나
        if (nums.size == 1) {
            return nums[0]
        }
        nums[1] = max(nums[0], nums[1])
        for (i in 2..nums.lastIndex) {
            nums[i] = max(nums[i - 1], nums[i - 2] + nums[i])
        }
        return nums.last()
    }
}
