package com.example;

import java.util.*;

public class MinimumHeightTrees310 {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int[] edge: edges) {
            map.putIfAbsent(edge[0], new ArrayList<>());
            map.putIfAbsent(edge[1], new ArrayList<>());
            map.get(edge[0]).add(edge[1]);
            map.get(edge[1]).add(edge[0]);
        }

        List<Integer> minHeightTrees = new ArrayList<>();
        for (Map.Entry<Integer, List<Integer>> entry : map.entrySet()) {
            if (entry.getValue().size() == 1) {
                minHeightTrees.add(entry.getKey());
            }
        }

        // 남은 노드가 3개 이상이라면 무조건 높이가 다른 노드가 있다
        // 1개 혹은 2개 노드만 최소 트리 높이를 가질 수 있다
        while (n > 2) {
            n -= minHeightTrees.size();
            List<Integer> newMinHeightTress = new ArrayList<>();
            for (int start : minHeightTrees) {
                // 연결된 노드가 1개 뿐인 노드라 0번째 인덱스 접근
                int end = map.get(start).get(0);
                map.get(end).remove((Object) start);
                if (map.get(end).size() == 1) {
                    newMinHeightTress.add(end);
                }
            }
            minHeightTrees = newMinHeightTress;
        }

        return minHeightTrees;
    }
}
