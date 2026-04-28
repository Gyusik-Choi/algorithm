package com.example;

import java.util.*;

public class CheapestFlightsWithinKStops787_4 {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        Map<Integer, List<int[]>> map = new HashMap<>();
        for (int[] flight : flights) {
            map.putIfAbsent(flight[0], new ArrayList<>());
            map.get(flight[0]).add(new int[]{flight[1], flight[2]});
        }
        int[] prices = new int[n];
        Arrays.fill(prices, Integer.MAX_VALUE);
        prices[src] = 0;
        Map<Integer, Integer> visited = new HashMap<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        // 정점, 비용, 경유
        pq.add(new int[]{src, 0, 0});

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            // 도착
            if (cur[0] == dst) {
                return cur[1];
            }
            // 추가 경유가 안 되는 경우 제외
            if (cur[2] > k) {
                continue;
            }
            // 이동이 가능하지만 최종 도착지의 비용보다 현재 더 비싼 경우 제외
            if (cur[1] > prices[dst]) {
                continue;
            }
            if (!map.containsKey(cur[0])) {
                continue;
            }
            visited.put(cur[0], cur[2]);
            // cur[0] 과 연결된 정점들
            for (int[] node : map.get(cur[0])) {
                if (node[0] != dst && cur[2] + 1 > k) {
                    continue;
                }
                if (visited.containsKey(node[0]) && visited.get(node[0]) < cur[2] + 1) {
                    continue;
                }
                pq.add(new int[]{node[0], cur[1] + node[1], cur[2] + 1});
            }
        }
        return -1;
    }
}
