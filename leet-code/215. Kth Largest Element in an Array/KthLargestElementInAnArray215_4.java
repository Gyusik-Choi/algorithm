package com.example;

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.stream.IntStream;

public class KthLargestElementInAnArray215_4 {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
        for (int num : nums) pq.add(num);
        IntStream.range(0, k - 1).forEach(i -> pq.poll());
        return pq.poll();
    }
}
