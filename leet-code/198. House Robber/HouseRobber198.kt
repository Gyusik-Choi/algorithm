package com.example

import kotlin.math.max

class HouseRobber198 {
    fun rob(nums: IntArray): Int {
        // 인접한 집을 털지 못하는 것 뿐이지 반드시 1칸씩 건너뛰어서 털어야 하는게 아니다
        // [1, 2, 3, 1]
        // [2, 7, 9, 3, 1]
        // [100, 1, 1, 100] -> [100, 100, 101, 200]
        // [100, 1, 2, 100, 5, 4, 100] -> [100, 100, 102, 200, 200, 204, 300]
        // dp 는 항상 최대값으로 갱신한다
        // 인접한 dp 값이 더 큰지 vs 두 칸 이전의 dp 값과 현재 값을 더하는게 더 큰지
        val dp = IntArray(nums.size)
        dp[0] = nums[0]
        if (nums.size == 1) {
            return dp[0]
        }
        dp[1] = max(nums[0], nums[1])
        if (nums.size == 2) {
            return dp[1]
        }
        for (i in 2 until nums.size) {
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        }
        return dp[nums.size - 1]
    }
}
