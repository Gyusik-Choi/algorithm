package com.example.algorithm;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSum15_5 {
    private static final int NOT_FOUND = 100001;

    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> list = new ArrayList<>();
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            for (int j = i + 1; j < nums.length - 1; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) {
                    continue;
                }
                int target = (nums[i] + nums[j]) * -1;
                int value = binarySearch(nums, target, j + 1, nums.length - 1);
                if (value != NOT_FOUND) {
                    list.add(Arrays.asList(nums[i], nums[j], value));
                }
            }
        }
        return list;
    }

    private int binarySearch(int[] nums, int target, int start, int end) {
        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (nums[mid] == target) {
                return nums[mid];
            }
            if (nums[mid] > target) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return NOT_FOUND;
    }
}
