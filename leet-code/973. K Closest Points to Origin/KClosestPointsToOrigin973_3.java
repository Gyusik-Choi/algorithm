package com.example;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.stream.IntStream;

public class KClosestPointsToOrigin973_3 {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingDouble(n -> n.dist));
        Arrays.stream(points).forEach(point -> pq.add(new Node(point)));
        int[][] answer = new int[k][2];
        IntStream.range(0, k).forEach(i -> answer[i] = pq.poll().point);
        return answer;
    }

    static class Node {
        int[] point;
        double dist;

        Node(int[] point) {
            this.point = point;
            this.dist = Math.sqrt(Math.pow(point[0], 2) + Math.pow(point[1], 2));
        }
    }
}
