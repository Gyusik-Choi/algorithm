package com.example;

import java.util.HashMap;
import java.util.Map;

public class IntersectionOfTwoArrays349 {
    public int[] intersection(int[] nums1, int[] nums2) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums1) map.put(num, 1);
        for (int num : nums2) if (map.containsKey(num)) map.put(num, 2);
        return map
                .entrySet()
                .stream()
                .filter(entry -> entry.getValue() == 2)
                .map(Map.Entry::getKey)
                .mapToInt(num -> num)
                .toArray();
    }
}
