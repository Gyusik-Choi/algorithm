package com.example;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MinimumHeightTrees310_2 {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        // 문제의 testcase 중에서 n이 1인 경우 [0] 여부를 검사하는 testcase 가 있다
        if (n == 1) return List.of(0);

        Map<Integer, List<Integer>> map = new HashMap<>();
        // 연결된 노드의 갯수
        int[] inDegree = new int[n];
        for (int[] edge: edges) {
            map.putIfAbsent(edge[0], new ArrayList<>());
            map.putIfAbsent(edge[1], new ArrayList<>());
            map.get(edge[0]).add(edge[1]);
            map.get(edge[1]).add(edge[0]);
            inDegree[edge[0]] += 1;
            inDegree[edge[1]] += 1;
        }

        List<Integer> minHeightTrees = new ArrayList<>();
        for (Map.Entry<Integer, List<Integer>> entry : map.entrySet()) {
            if (entry.getValue().size() == 1) minHeightTrees.add(entry.getKey());
        }

        while (true) {
            List<Integer> newMinHeightTress = new ArrayList<>();
            for (int start : minHeightTrees) {
                for (Integer end : map.get(start)) {
                    inDegree[end] -= 1;
                    if (inDegree[end] == 1) newMinHeightTress.add(end);
                }
            }
            // 더 이상 다른 1개의 노드와 연결된 노드가 없는 경우
            // 이전에 구한 newMinHeightTress 이 정답이 된다
            // 이전에 구한 newMinHeightTress 의 값이 유일하게 남은
            // 다른 1개의 노드와 연결된 노드였으나
            // inDegree 를 1씩 빼면서 0이 되어 연결된 노드가 없어졌다
            if (newMinHeightTress.isEmpty()) break;
            minHeightTrees = newMinHeightTress;
        }

        return minHeightTrees;
    }
}
