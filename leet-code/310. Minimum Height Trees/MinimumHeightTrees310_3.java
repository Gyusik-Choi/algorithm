package com.example;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MinimumHeightTrees310_3 {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n == 1) {
            return List.of(0);
        }

        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int[] edge : edges) {
            map.putIfAbsent(edge[0], new ArrayList<>());
            map.putIfAbsent(edge[1], new ArrayList<>());
            map.get(edge[0]).add(edge[1]);
            map.get(edge[1]).add(edge[0]);
        }

        List<Integer> leaves = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (!map.containsKey(i) || map.get(i).size() == 1) {
                leaves.add(i);
            }
        }

        while (n > 2) {
            List<Integer> newLeaves = new ArrayList<>();
            for (int leaf : leaves) {
                Integer neighbor = map.get(leaf).get(0);
                map.get(neighbor).remove((Object) leaf);
                if (map.get(neighbor).size() == 1) {
                    newLeaves.add(neighbor);
                }
                map.remove(leaf);
            }
            n -= leaves.size();
            leaves = newLeaves;
        }

        return leaves;
    }
}
