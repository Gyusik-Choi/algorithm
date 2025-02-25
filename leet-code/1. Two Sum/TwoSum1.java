package com.example;

import java.util.Arrays;
import java.util.Comparator;

public class TwoSum1 {

    public int[] twoSum(int[] nums, int target) {
        int[][] numsWithIdx = new int[nums.length][2];
        for (int i = 0; i < nums.length; i++) {
            numsWithIdx[i][0] = nums[i];
            numsWithIdx[i][1] = i;
        }
        // 정렬 후 two pointer
        int left = 0, right = nums.length - 1;
        Arrays.sort(numsWithIdx, Comparator.comparingInt(o -> o[0]));
        while (left < right) {
            int sum = numsWithIdx[left][0] + numsWithIdx[right][0];
            if (sum == target) break;
            if (sum < target) left += 1;
            else right -= 1;
        }
        return new int[]{numsWithIdx[left][1], numsWithIdx[right][1]};
    }
}
