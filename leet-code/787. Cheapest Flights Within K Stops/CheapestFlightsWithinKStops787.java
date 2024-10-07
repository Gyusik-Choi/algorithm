import org.jetbrains.annotations.NotNull;

import java.util.*;

public class CheapestFlightsWithinKStops787 {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        // 정점 인접 리스트
        // 거리
        // 방문
        // 우선순위 큐 (Flight 객체)
        Map<Integer, List<Flight>> map = new HashMap<>();
        for (int[] flight : flights) {
            map.putIfAbsent(flight[0], new ArrayList<>());
            map.get(flight[0]).add(new Flight(flight[2], 0, flight[1]));
        }
        return dijkstra(n, src, dst, k, map);
    }

    private int dijkstra(int n, int src, int dst, int k, Map<Integer, List<Flight>> map) {
        Map<Integer, Integer> visit = new HashMap<>();
        Queue<Flight> pq = new PriorityQueue<>();
        pq.add(new Flight(0, 0, src));

        while (!pq.isEmpty()) {
            Flight start = pq.poll();
            if (start.source == dst) return start.cost;
            if (start.stop > k) continue;
            if (!map.containsKey(start.source)) continue;
            visit.put(start.source, start.stop);

            for (Flight end : map.get(start.source)) {
                if (visit.containsKey(end.source) && visit.get(end.source) < start.stop + 1) continue;
                pq.add(new Flight(start.cost + end.cost, start.stop + 1, end.source));
            }
        }
        return -1;
    }

    private static class Flight implements Comparable<Flight> {
        int cost;
        int stop;
        int source;

        public Flight(int cost, int stop, int source) {
            this.cost = cost;
            this.stop = stop;
            this.source = source;
        }

        @Override
        public int compareTo(@NotNull Flight o) {
            return this.cost == o.cost ? this.stop - o.stop : this.cost - o.cost;
        }
    }
}
