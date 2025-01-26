package com.example.algorithm;

public class MaximumSubarray53_2 {

    public int maxSubArray(int[] nums) {
        int currentSum = 0;
        int bestSum = Integer.MIN_VALUE;
        for (int num : nums) {
            currentSum = Math.max(currentSum + num, num);
            bestSum = Math.max(bestSum, currentSum);
        }
        return bestSum;
    }
}
