package com.example;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class KClosestPointsToOrigin973_4 {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingDouble(this::getSqrt));
        pq.addAll(Arrays.asList(points));
        int[][] answer = new int[k][2];
        for (int i = 0; i < k; i++) {
            answer[i] = pq.poll();
        }
        return answer;
    }

    private double getSqrt(int[] point) {
        return Math.sqrt(Math.pow(point[0], 2) + Math.pow(point[1], 2));
    }
}
