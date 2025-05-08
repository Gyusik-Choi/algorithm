package com.example;

import java.util.*;

public class CheapestFlightsWithinKStops787_2 {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        Map<Integer, List<int[]>> map = new HashMap<>();
        for (int[] flight : flights) {
            int start = flight[0];
            int end = flight[1];
            int cost = flight[2];
            map.putIfAbsent(start, new ArrayList<>());
            map.get(start).add(new int[]{end, cost});
        }

        int[] stops = new int[n];
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(src, 0, 0));

        while (!pq.isEmpty()) {
            Node departure = pq.poll();

            if (departure.from == dst) {
                return departure.price;
            }

            stops[departure.from] = departure.stop;

            if (departure.stop > k) {
                continue;
            }

            if (!map.containsKey(departure.from)) {
                continue;
            }

            for (int[] node : map.get(departure.from)) {
                int arrival = node[0];
                int price = node[1];
                // 비용은 고려하지 않는다
                if (stops[arrival] == 0 || (stops[arrival] > 0 && stops[arrival] > departure.stop + 1)) {
                    pq.add(new Node(arrival, departure.price + price, departure.stop + 1));
                }
            }
        }

        return -1;
    }

    private static class Node implements Comparable<Node> {
        int from;
        int price;
        int stop;

        @Override
        public int compareTo(Node o) {
            return this.price - o.price;
        }

        Node(int from, int price, int stop) {
            this.from = from;
            this.price = price;
            this.stop = stop;
        }
    }
}
