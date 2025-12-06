package com.example;

import java.util.*;
import java.util.stream.IntStream;

public class MstPrim {
    // 정점 갯수, [출발, 도착, 비용]
    // 정점은 1부터 n까지로 구성
    public int mst(int n, int[][] data) {
        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o.cost));
        Map<Integer, List<Node>> map = new HashMap<>();
        boolean[] visited = new boolean[n + 1];

        for (int[] d : data) {
            map.putIfAbsent(d[0], new ArrayList<>());
            map.putIfAbsent(d[1], new ArrayList<>());
            map.get(d[0]).add(new Node(d[0], d[1], d[2]));
            map.get(d[1]).add(new Node(d[1], d[0], d[2]));
        }
        // 임의의 시작점으로 1을 선택
        pq.add(new Node(0, 1, 0));
        int total = 0;

        while (!pq.isEmpty()) {
            Node node = pq.poll();
            if (visited[node.end]) {
                continue;
            }
            total += node.cost;
            visited[node.end] = true;
            if (isAllConnected(visited)) {
                break;
            }
            for (Node end : map.get(node.end)) {
                if (visited[end.end]) {
                    continue;
                }
                pq.add(end);
            }
        }
        return total;
    }

    private boolean isAllConnected(boolean[] visit) {
        return IntStream.range(1, visit.length).allMatch(i -> visit[i]);
    }

    private static class Node {
        int start;
        int end;
        int cost;

        Node(int start, int end, int cost) {
            this.start = start;
            this.end = end;
            this.cost = cost;
        }
    }
}
