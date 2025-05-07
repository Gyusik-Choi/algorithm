package com.example;

import java.util.*;

public class NetworkDelayTime743_2 {
    public int networkDelayTime(int[][] times, int n, int k) {
        Map<Integer, List<Node>> map = new HashMap<>();
        for (int[] time : times) {
            int start = time[0];
            int end = time[1];
            int delay = time[2];
            map.putIfAbsent(start, new ArrayList<>());
            map.get(start).add(new Node(end, delay));
        }

        int[] delayTimes = dijkstra(map, n, k);
        int maxTime = 0;
        for (int i = 1; i < n + 1; i++) {
            if (delayTimes[i] == Integer.MAX_VALUE) {
                return -1;
            }
            maxTime = Math.max(maxTime, delayTimes[i]);
        }
        return maxTime;
    }

    private int[] dijkstra(Map<Integer, List<Node>> map, int n, int k) {
        int[] delayTime = new int[n + 1];
        boolean[] visited = new boolean[n + 1];
        for (int i = 0; i < n + 1; i++) {
            delayTime[i] = Integer.MAX_VALUE;
        }

        PriorityQueue<Node> pq = new PriorityQueue<>();
        delayTime[k] = 0;
        pq.add(new Node(k, delayTime[k]));

        while (!pq.isEmpty()) {
            Node departure = pq.poll();

            if (visited[departure.label]) {
                continue;
            }

            visited[departure.label] = true;

            if (!map.containsKey(departure.label)) {
                continue;
            }

            for (Node arrival : map.get(departure.label)) {
                if (visited[arrival.label]) {
                    continue;
                }

                if (departure.time + arrival.time >= delayTime[arrival.label]) {
                    continue;
                }

                delayTime[arrival.label] = departure.time + arrival.time;
                arrival.time = delayTime[arrival.label];
                pq.add(arrival);
            }
        }
        return delayTime;
    }

    private static class Node implements Comparable<Node> {
        int label;
        int time;

        Node(int label, int time) {
            this.label = label;
            this.time = time;
        }

        @Override
        public int compareTo(Node o) {
            return this.time - o.time;
        }
    }
}
