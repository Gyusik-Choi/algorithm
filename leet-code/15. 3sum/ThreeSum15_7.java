package com.example;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSum15_7 {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> answer = new ArrayList<>();
        for (int i = 0; i < nums.length - 2; i++) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i - 1] == nums[i]) continue;
            int left = i + 1, right = nums.length - 1;
            int target = -(nums[i]);
            while (left < right) {
                while (left < right && left > i + 1 && nums[left - 1] == nums[left]) left++;
                while (left < right && right < nums.length - 1 && nums[right] == nums[right + 1]) right--;
                if (left >= right) break;
                int sum = nums[left] + nums[right];
                if (target == sum) {
                    answer.add(List.of(nums[i], nums[left], nums[right]));
                    left++;
                    right--;
                    continue;
                }
                if (sum > target) right--;
                else left++;
            }
        }
        return answer;
    }
}
