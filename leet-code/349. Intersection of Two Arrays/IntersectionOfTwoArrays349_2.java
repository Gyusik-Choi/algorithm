package com.example;

import java.util.*;

public class IntersectionOfTwoArrays349_2 {
    public int[] intersection(int[] nums1, int[] nums2) {
        Arrays.sort(nums2);
        Set<Integer> answer = new HashSet<>();
        for (int num : nums1) if (containsInt(nums2, num)) answer.add(num);
        return answer.stream().mapToInt(i -> i).toArray();
    }

    private boolean containsInt(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) return true;
            if (nums[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return false;
    }
}
