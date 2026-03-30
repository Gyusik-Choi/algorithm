package com.example;

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class TopKFrequentElements347_5 {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        PriorityQueue<Element> pq = new PriorityQueue<>((o1, o2) -> o2.value - o1.value);
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            pq.add(new Element(entry.getKey(), entry.getValue()));
        }
        int[] answer = new int[k];
        for (int i = 0; i < k; i++) {
            answer[i] = pq.poll().key;
        }
        return answer;
    }

    private static class Element {
        private final int key;
        private final int value;

        private Element(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }
}
