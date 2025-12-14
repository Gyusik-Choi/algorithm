package com.example;

import java.util.PriorityQueue;

public class SlidingWindowMaximum239_2 {
    public int[] maxSlidingWindow(int[] nums, int k) {
        PriorityQueue<Item> pq = new PriorityQueue<>((o1, o2) -> o2.num - o1.num);
        for (int i = 0; i < k - 1; i++) {
            pq.add(new Item(nums[i], i));
        }
        int[] answer = new int[nums.length - k + 1];
        for (int i = 0; i < nums.length - k + 1; i++) {
            pq.add(new Item(nums[k + i - 1], k + i - 1));
            while (pq.peek().idx < i) {
                pq.poll();
            }
            answer[i] = pq.peek().num;
        }
        return answer;
    }

    private static class Item {
        public final int num;
        public final int idx;

        public Item(int num, int idx) {
            this.num = num;
            this.idx = idx;
        }
    }
}
