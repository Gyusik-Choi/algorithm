package com.example;

import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.stream.IntStream;

public class KthLargestElementInAnArray215 {
    public int findKthLargest(int[] nums, int k) {
        Queue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());
        for (int num : nums) queue.add(num);
        IntStream.range(0, k).forEach(i -> queue.poll());
        return queue.poll();
    }
}
