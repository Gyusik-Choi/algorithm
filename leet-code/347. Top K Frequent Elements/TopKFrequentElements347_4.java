package com.example;

import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;

public class TopKFrequentElements347_4 {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        Arrays.stream(nums)
                .forEach(num -> count.put(num, count.getOrDefault(num, 0) + 1));
        return count.keySet().stream()
                .sorted((o1, o2) -> count.get(o2) - count.get(o1))
                .limit(k)
                .mapToInt(n -> n)
                .toArray();
    }
}
