package com.example

import kotlin.math.max

class HouseRobber198_3 {
    fun rob(nums: IntArray): Int {
        val dp = IntArray(nums.size + 1)
        dp[1] = nums[0]
        for (i in 1 until nums.size) dp[i + 1] = max(dp[i - 1] + nums[i], dp[i])
        return dp[nums.size]
    }
}
