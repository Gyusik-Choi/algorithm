package com.example;

import java.util.Arrays;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.stream.IntStream;

public class KthLargestElementInAnArray215_3 {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        Arrays.stream(nums).forEach(pq::offer);
        IntStream.range(1, k).forEach(i -> pq.poll());
        return pq.poll();
    }
}
