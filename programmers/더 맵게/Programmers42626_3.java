package com.example;

import java.util.Arrays;
import java.util.PriorityQueue;

public class Programmers42626_3 {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        Arrays.stream(scoville).forEach(pq::add);
        int count = 0;
        while (pq.size() > 1) {
            int first = pq.poll();
            if (first >= K) {
                return count;
            }
            int second = pq.poll();
            pq.add(first + second * 2);
            count += 1;
        }
        if (pq.size() == 1 && pq.peek() >= K) {
            return count;
        }
        return pq.isEmpty()
                ? count
                : -1;
    }
}
