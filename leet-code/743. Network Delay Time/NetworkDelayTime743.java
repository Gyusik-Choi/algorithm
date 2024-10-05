import java.util.*;

public class NetworkDelayTime743 {
    public int networkDelayTime(int[][] times, int n, int k) {
        Map<Integer, List<Integer[]>> map = new HashMap<>();
        for (int[] time : times) {
            map.putIfAbsent(time[0], new ArrayList<>());
            map.get(time[0]).add(new Integer[]{time[1], time[2]});
        }
        int[] distance = dijkstra(map, n, k);
        return isNotConnected(distance) ? -1 : getMaxValue(distance);
    }

    private int[] dijkstra(Map<Integer, List<Integer[]>> map, int maxNum, int start) {
        int[] distance = new int[maxNum + 1];
        boolean[] visit = new boolean[maxNum + 1];
        PriorityQueue<Integer[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[1]));

        int maxValue = Integer.MAX_VALUE;
        for (int i = 1; i <= maxNum; i++) distance[i] = maxValue;
        distance[0] = 0;
        distance[start] = 0;
        pq.add(new Integer[]{start, distance[start]});

        while (!pq.isEmpty()) {
            Integer[] startNode = pq.poll();
            if (visit[startNode[0]]) continue;
            visit[startNode[0]] = true;
            if (!map.containsKey(startNode[0])) continue;
            for (Integer[] endNode : map.get(startNode[0])) {
                if (visit[endNode[0]]) continue;
                if (distance[endNode[0]] < startNode[1] + endNode[1]) continue;
                distance[endNode[0]] = startNode[1] + endNode[1];
                pq.add(new Integer[]{endNode[0], distance[endNode[0]]});
            }
        }

        return distance;
    }

    private boolean isNotConnected(int[] distance) {
        return Arrays
                .stream(distance)
                .anyMatch(d -> d == Integer.MAX_VALUE);
    }

    private int getMaxValue(int[] distance) {
        return Arrays
                .stream(distance)
                .max()
                .getAsInt();
    }
}
