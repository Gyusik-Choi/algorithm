package com.example;

import java.util.*;

public class CheapestFlightsWithinKStops787_3 {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        Map<Integer, List<Node>> map = new HashMap<>();
        Arrays.stream(flights).forEach(flight -> {
            map.putIfAbsent(flight[0], new ArrayList<>());
            map.get(flight[0]).add(new Node(flight[1], flight[2], 0));
        });
        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o.price));
        pq.offer(new Node(src, 0, 0));
        Map<Integer, Integer> visited = new HashMap<>();
        while (!pq.isEmpty()) {
            Node start = pq.poll();
            if (start.num == dst) {
                return start.price;
            }
            if (start.stop > k) {
                continue;
            }
            if (!map.containsKey(start.num)) {
                continue;
            }
            visited.put(start.num, start.stop);
            for (Node end : map.get(start.num)) {
                if (!visited.containsKey(end.num) || visited.get(end.num) > start.stop) {
                    pq.offer(new Node(end.num, start.price + end.price, start.stop + 1));
                }
            }
        }
        return -1;
    }

    static class Node {
        int num;
        int price;
        int stop;

        Node(int num, int price, int stop) {
            this.num = num;
            this.price = price;
            this.stop = stop;
        }
    }
}
