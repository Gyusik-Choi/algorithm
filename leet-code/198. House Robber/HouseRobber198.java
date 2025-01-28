package com.example.algorithm;

import java.util.Arrays;

public class HouseRobber198 {

    public int rob(int[] nums) {
        int[] dp = new int[nums.length];
        if (nums.length == 1) return nums[0];
        if (nums.length == 2) return Math.max(nums[0], nums[1]);
        dp[0] = nums[0];
        dp[1] = nums[1];
        // 아래의 코드는
        // return 문에서 최대값을 구하기 때문에 통과할 수 있었고
        // 실제로는 잘못된 코드다
        // 올바른 dp[2] 의 값은 Math.max(nums[0] + nums[2], nums[1])
        // nums[0] + nums[2] 와 nums[1] 중에 더 큰 값이다
        dp[2] = nums[0] + nums[2];
        for (int i = 3; i < nums.length; i++)
            dp[i] = Math.max(dp[i - 2], dp[i - 3]) + nums[i];
        return Arrays.stream(dp).max().getAsInt();
    }
}
