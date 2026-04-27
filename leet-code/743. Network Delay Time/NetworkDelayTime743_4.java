package com.example;

import java.util.*;

public class NetworkDelayTime743_4 {
    public int networkDelayTime(int[][] times, int n, int k) {
        // 다익스트라
        // 연결되지 않은 정점이 있으면 -1
        Map<Integer, List<int[]>> map = new HashMap<>();
        for (int[] time : times) {
            map.putIfAbsent(time[0], new ArrayList<>());
            map.get(time[0]).add(new int[]{time[1], time[2]});
        }
        int[] minTimes = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            minTimes[i] = Integer.MAX_VALUE;
        }
        minTimes[k] = 0;
        boolean[] visit = new boolean[n + 1];
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[1]));
        pq.add(new int[]{k, 0});
        while (!pq.isEmpty()) {
            int[] node = pq.poll();
            if (visit[node[0]]) {
                continue;
            }
            visit[node[0]] = true;
            if (map.containsKey(node[0])) {
                for (int[] dest : map.get(node[0])) {
                    if (visit[dest[0]]) {
                        continue;
                    }
                    if (node[1] + dest[1] > minTimes[dest[0]]) {
                        continue;
                    }
                    minTimes[dest[0]] = node[1] + dest[1];
                    pq.add(new int[]{dest[0], minTimes[dest[0]]});
                }
            }
        }
        int maxDelayTime = 0;
        for (int i = 1; i <= n; i++) {
            maxDelayTime = Math.max(maxDelayTime, minTimes[i]);
        }
        return maxDelayTime == Integer.MAX_VALUE ? -1 : maxDelayTime;
    }
}
