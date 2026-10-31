package com.example;

import java.util.PriorityQueue;

public class Programmers42626_4 {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int s : scoville) pq.add(s);
        int cnt = 0;
        while (pq.size() >= 2 && pq.peek() < K) {
            Integer first = pq.poll();
            Integer second = pq.poll();
            pq.add(first + (second * 2));
            cnt += 1;
        }
        return pq.isEmpty() || pq.peek() < K ? -1 : cnt;
    }
}
