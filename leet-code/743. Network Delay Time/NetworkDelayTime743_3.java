package com.example;

import java.util.*;

public class NetworkDelayTime743_3 {
    public int networkDelayTime(int[][] times, int n, int k) {
        Map<Integer, List<Node>> map = new HashMap<>();
        Arrays.stream(times).forEach(time -> {
            map.putIfAbsent(time[0], new ArrayList<>());
            map.get(time[0]).add(new Node(time[1], time[2]));
        });
        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o.time));
        pq.offer(new Node(k, 0));
        boolean[] visited = new boolean[n + 1];
        int[] minTime = new int[n + 1];
        Arrays.fill(minTime, Integer.MAX_VALUE);
        minTime[k] = 0;

        while (!pq.isEmpty()) {
            Node start = pq.poll();
            if (visited[start.num]) {
                continue;
            }
            visited[start.num] = true;

            if (!map.containsKey(start.num)) {
                continue;
            }
            for (Node end : map.get(start.num)) {
                if (visited[end.num]) {
                    continue;
                }
                if (minTime[end.num] <= start.time + end.time) {
                    continue;
                }
                minTime[end.num] = start.time + end.time;
                pq.offer(new Node(end.num, minTime[end.num]));
            }
        }

        if (unableToTransmitToAllNodes(minTime, 1, n)) {
            return -1;
        }

        return getMaxValue(minTime, 1, n);
    }

    private boolean unableToTransmitToAllNodes(int[] time, int start, int end) {
        return Arrays.stream(time, start, end + 1)
                .filter(val -> val == Integer.MAX_VALUE)
                .findAny()
                .isPresent();
    }

    private int getMaxValue(int[] time, int start, int end) {
        return Arrays.stream(time, start, end + 1)
                .max()
                .getAsInt();
    }

    static class Node {
        public int num;
        public int time;

        public Node(int num, int time) {
            this.num = num;
            this.time = time;
        }
    }
}
