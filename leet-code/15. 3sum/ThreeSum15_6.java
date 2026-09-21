package com.example;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSum15_6 {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> answer = new ArrayList<>();
        for (int i = 0; i < nums.length - 2; i++) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i - 1] == nums[i]) continue;
            for (int j = i + 1; j < nums.length - 1; j++) {
                if (nums[i] + nums[j] > 0) break;
                if (j > i + 1 && nums[j - 1] == nums[j]) continue;
                int target = -(nums[i] + nums[j]);
                int k = binarySearch(nums, j + 1, target);
                if (k != -1) answer.add(List.of(nums[i], nums[j], nums[k]));
            }
        }
        return answer;
    }

    private int binarySearch(int[] nums, int startIdx, int target) {
        int left = startIdx, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return -1;
    }
}
