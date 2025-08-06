package com.example

import java.lang.Integer.max

class MaximumSubarray53 {
    fun maxSubArray(nums: IntArray): Int {
        // dp
        // 직전 값이 본인과 더했을 때
        // 본인보다 더 크면 더하고 본인보다 더 작으면 본인을 선택
        val dp = IntArray(nums.size)
        dp[0] = nums[0]
        for (i in 1 until nums.size) {
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        }
        return dp.max()
    }
}
