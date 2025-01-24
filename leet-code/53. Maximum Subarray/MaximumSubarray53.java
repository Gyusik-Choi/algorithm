package com.example;

import java.util.Arrays;

public class MaximumSubarray53 {

    public int maxSubArray(int[] nums) {
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        for (int i = 1; i < nums.length; i++) dp[i] = Math.max(nums[i], dp[i - 1] + nums[i]);
        return Arrays.stream(dp).max().getAsInt();
    }
}

// -2                       -> -2
// -2 1                     -> 1
// -2 1 -3                  -> 1
// -2 1 -3 4                -> 4
// -2 1 -3 4 -1             -> 4
// -2 1 -3 4 -1 2           -> 5 (4 -1 2)
// -2 1 -3 4 -1 2 1         -> 6 (4 -1 2 1)
// -2 1 -3 4 -1 2 1 -5      -> 6 (4 -1 2 1)
// -2 1 -3 4 -1 2 1 -5 4    -> 6 (4 -1 2 1)
//
// 1) 총합보다 현재값이 더 큰 경우
// 1-1) 총합이 음수면
// 기존 범위 버리고 총합을 현재값으로 설정
// 1-2) 총합이 양수면
// 총합에 더하고 총합 범위 확대
// 2) 총합보다 현재값이 더 작은 경우
// 2-1)
// 2-1-1)
// 2-1-2)
// 총합은 유지하면서 현재값 이후의 범위를 새로 탐색할 수 있도록
// left, right 를 현재값 이후로 설정
// 2-2) 총합에서 현재값을 더했을때 총합이 감소하면
// 뒤에 더 큰 값이 나올 수 있으므로
// 기존 범위에서 총합에 더하고 기존 범위에서 확대 (총합 범위 유지)
// 2-3) 총합에서 현재값을 더했을때 총합이 증가하면
// 총합에 더하고 총합 범위 확대
// 3) 총합과 현재값이 같은 경우
// 3-1) 총합이 음수면
// 기존 범위
//
// (left, right 모두 이동)
// 더했을때 총합보다 크면 범위 확대
// int largestSum = Integer.MIN_VALUE;
// int left = 0, right = 0;
// int start = 0, end = 0;
// left 와 right 로 이동하고
// start 와 end 로 subarray 범위를 나타낸다
//
// 총합 vs 현재값
//