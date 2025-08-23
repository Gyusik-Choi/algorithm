package com.example;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSum15_4 {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> answer = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i - 1] == nums[i]) {
                continue;
            }
            int left = i + 1, right = nums.length - 1;
            while (left < right) {
                int sum = getSum(nums, i, left, right);
                if (sum == 0) {
                    answer.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    while (left < right && nums[left] == nums[left + 1]) {
                        left += 1;
                    }
                    while (left < right && nums[right] == nums[right - 1]) {
                        right -= 1;
                    }
                    left += 1;
                    right -= 1;
                    continue;
                }

                if (sum < 0) {
                    while (left < right && nums[left] == nums[left + 1]) {
                        left += 1;
                    }
                    left += 1;
                } else {
                    while (left < right && nums[right] == nums[right - 1]) {
                        right -= 1;
                    }
                    right -= 1;
                }
            }
        }

        return answer;
    }

    private int getSum(int[] nums, int left, int mid, int right) {
        return nums[left] + nums[mid] + nums[right];
    }
}
