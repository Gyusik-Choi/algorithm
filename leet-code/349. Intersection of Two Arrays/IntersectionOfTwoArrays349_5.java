package com.example;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class IntersectionOfTwoArrays349_5 {
    public int[] intersection(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Set<Integer> set = new HashSet<>();
        for (int num2 : nums2) {
            if (exist(nums1, num2)) {
                set.add(num2);
            }
        }
        return set.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }

    private boolean exist(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == target) {
                return true;
            }
            if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return false;
    }
}
