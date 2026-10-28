package com.example;

import java.util.Comparator;
import java.util.PriorityQueue;

public class KClosestPointsToOrigin973_5 {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<Point> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a.dist));
        for (int[] point : points) pq.add(new Point(point));
        int[][] answer = new int[k][];
        for (int i = 0; i < k; i++) answer[i] = pq.poll().arr;
        return answer;
    }

    static class Point {
        private final int[] arr;
        private final int dist;

        private Point(int[] arr) {
            this.arr = arr;
            this.dist = (arr[0] * arr[0]) + (arr[1] * arr[1]);
        }
    }
}
