package com.example;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

public class QueueReconstructionByHeight406_2 {
    public int[][] reconstructQueue(int[][] people) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] == b[0] ? a[1] - b[1] : b[0] - a[0]);
        pq.addAll(Arrays.asList(people));
        List<int[]> answer = new ArrayList<>();
        while (!pq.isEmpty()) {
            int[] item = pq.poll();
            answer.add(item[1], item);
        }
        return answer.toArray(new int[0][0]);
    }
}
