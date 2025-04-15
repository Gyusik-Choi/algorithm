package com.example;

import java.util.Comparator;
import java.util.PriorityQueue;

public class Programmers42626_2 {

    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.comparingInt(x -> x));
        for (int x : scoville) {
            pq.offer(x);
        }

        int cnt = 0;
        while (pq.size() >= 2) {
            if (pq.peek() >= K) {
                break;
            }

            int food = pq.poll();
            int food2 = pq.poll();
            pq.add(food + (food2 * 2));
            cnt += 1;
        }

        return !pq.isEmpty() && pq.peek() < K
                ? -1
                : cnt;
    }
}
