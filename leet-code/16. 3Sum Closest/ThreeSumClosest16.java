package com.example;

import java.util.Arrays;

public class ThreeSumClosest16 {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int closest = 100000;
        for (int i = 0; i < nums.length - 2; i++) {
            int j = i + 1, k = nums.length - 1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == target) return target;
                if (Math.abs(target - closest) > Math.abs(target - sum)) {
                    closest = sum;
                }
                if (sum < target) j++;
                else k--;
            }
        }
        return closest;
    }
}
