import java.util.*;

public class NetworkDelayTime743_3 {
    public int networkDelayTime(int[][] times, int n, int k) {
        // 기존 풀이와 차이는 Map 의 value 를 List 가 아니라 Map 으로 둔다
        // 출발점과 도착점의 한 쌍이 여러개가 나오지 않고 한개만 나온다는 조건이 있어서 가능
        Map<Integer, Map<Integer, Integer>> map = new HashMap<>();
        for (int[] time : times) {
            map.putIfAbsent(time[0], new HashMap<>());
            map.get(time[0]).put(time[1], time[2]);
        }
        // 기존 풀이는 거리 정보를 나타내는 배열, 중복 방문을 막기 위한 방문 배열을 뒀는데
        // 이 풀이는 거리 및 방문 정보를 함께 나타내는 Map 하나로 해결한다
        // 그리고 기존 풀이는 우선순위 큐에 도착지, 거리 정보를 나타내는 배열을 넣었는데
        // 이 풀이는 우선순위 큐에 Map 을 넣는다
        Queue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>(Map.Entry.comparingByValue());
        pq.add(new AbstractMap.SimpleEntry<>(k, 0));
        Map<Integer, Integer> dist = new HashMap<>();

        while (!pq.isEmpty()) {
            Map.Entry<Integer, Integer> startNode = pq.poll();
            int start = startNode.getKey();
            int startDist = startNode.getValue();

            if (dist.containsKey(start)) continue;
            dist.put(start, startDist);

            if (!map.containsKey(start)) continue;
            for (Map.Entry<Integer, Integer> entry : map.get(start).entrySet()) {
                int end = entry.getKey();
                int endDist = entry.getValue();
                // 기존 풀이는 거리 값을 갱신할 수 있는지 여부를 검사했는데
                // 이 풀이는 검사하지 않고 우선순위 큐에 넣는다
                // 우선순위 큐의 정렬에 의해 해당 노드로의 가장 가까운 거리 정보가 꺼내질거라
                // 별도의 검사없이 우선순위 큐에 바로 넣는다
                pq.add(new AbstractMap.SimpleEntry<>(end, startDist + endDist));
            }
        }

        // 기존 풀이와 달리 거리가 갱신되지 않은 정점이 있는지 확인하지 않고
        // dist 의 크기가 n 과 같은지 여부로 모든 정점을 갈 수 있는지 확인할 수 있다
        // 그리고 최대값을 기존 풀이와 달리 Stream 이 아닌 Collections 의 max 함수로 보다 간결하게 구한다
        return dist.size() == n ? Collections.max(dist.values()) : -1;
    }
}
