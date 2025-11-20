package com.example;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class IntersectionOfTwoArrays349_4 {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> set = new HashSet<>();
        Arrays.sort(nums1);
        for (int num : nums2) {
            if (contains(nums1, num)) {
                set.add(num);
            }
        }
        return set.stream().mapToInt(Integer::intValue).toArray();
    }

    private boolean contains(int[] arr, int num) {
        int left = 0, right = arr.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == num) {
                return true;
            }
            if (arr[mid] < num) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return false;
    }
}
