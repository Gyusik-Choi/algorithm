package com.example.algorithm;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class ThreeSum15_4 {

    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        Set<List<Integer>> result = new HashSet<>();
        for (int i = 0; i < nums.length - 2; i++) {
            for (int j = i + 1; j < nums.length - 1; j++) {
                if (i > 0 && nums[i] == nums[i - 1] && nums[i] == nums[j]) continue;
                int left = j + 1;
                int right = nums.length - 1;
                while (left <= right) {
                    int mid = (left + right) / 2;
                    int sum = nums[i] + nums[mid] + nums[j];
                    if (sum == 0) {
                        result.add(Arrays.asList(nums[i], nums[mid], nums[j]));
                        if (mid - 1 >= 0 && nums[mid] == nums[mid - 1]) break;
                    }

                    if (sum >= 0) right = mid - 1;
                    else left = mid + 1;
                }
            }
        }
        return result.stream().toList();
    }
}
