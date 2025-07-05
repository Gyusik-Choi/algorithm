package com.example;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class IntersectionOfTwoArrays349_3 {
    public int[] intersection(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int i = 0, j = 0;
        Set<Integer> set = new HashSet<>();
        while (i < nums1.length && j < nums2.length) {
            if (nums1[i] == nums2[j]) {
                set.add(nums1[i]);
                i += 1;
                j += 1;
            } else if (nums1[i] < nums2[j]) {
                i += 1;
            } else {
                j += 1;
            }
        }
        return set.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }
}
