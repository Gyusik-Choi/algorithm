package com.example;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MinimumHeightTrees310_4 {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n == 1) {
            return List.of(0);
        }
        Map<Integer, List<Integer>> map = new HashMap<>();
        Map<Integer, Integer> level = new HashMap<>();
        for (int[] edge : edges) {
            map.putIfAbsent(edge[0], new ArrayList<>());
            map.putIfAbsent(edge[1], new ArrayList<>());
            map.get(edge[0]).add(edge[1]);
            map.get(edge[1]).add(edge[0]);
            level.put(edge[0], level.getOrDefault(edge[0], 0) + 1);
            level.put(edge[1], level.getOrDefault(edge[1], 0) + 1);
        }
        while (level.size() > 2) {
            List<Integer> starts = findStarts(level);
            for (Integer start : starts) {
                level.remove(start);
                if (!map.containsKey(start)) {
                    continue;
                }
                for (int end : map.get(start)) {
                    if (!level.containsKey(end)) {
                        continue;
                    }
                    level.put(end, level.get(end) - 1);
                }
            }
        }
        return level.keySet().stream().toList();
    }

    private List<Integer> findStarts(Map<Integer, Integer> nodes) {
        return nodes.entrySet().stream()
                .filter(entry -> entry.getValue() == 1)
                .map(Map.Entry::getKey)
                .toList();
    }
}
