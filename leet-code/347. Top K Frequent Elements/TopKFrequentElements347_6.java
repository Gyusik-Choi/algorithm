package com.example;

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.stream.IntStream;

public class TopKFrequentElements347_6 {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) map.put(num, map.getOrDefault(num, 0) + 1);
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> b[1] - a[1]);
        map.forEach((key, value) -> pq.add(new int[]{key, value}));
        return IntStream.range(0, k).map(i -> pq.poll()[0]).toArray();
    }
}
