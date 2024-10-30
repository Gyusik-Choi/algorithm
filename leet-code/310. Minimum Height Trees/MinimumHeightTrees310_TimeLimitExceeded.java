package com.example;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MinimumHeightTrees310_TimeLimitExceeded {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int[] edge: edges) {
            map.putIfAbsent(edge[0], new ArrayList<>());
            map.putIfAbsent(edge[1], new ArrayList<>());
            map.get(edge[0]).add(edge[1]);
            map.get(edge[1]).add(edge[0]);
        }

        List<Integer> minHeightTrees = new ArrayList<>();
        minHeightTrees.add(Integer.MAX_VALUE);
        for (int i = 0; i < n; i++) {
            boolean[] visit = new boolean[n];
            visit[i] = true;
            treeHeight = 0;
            getTreeHeight(i, map, visit, 0);
            if (minTreeHeight > treeHeight) {
                minHeightTrees = new ArrayList<>();
                minHeightTrees.add(i);
            } else if (minTreeHeight == treeHeight) {
                minHeightTrees.add(i);
            }
            minTreeHeight = Math.min(minTreeHeight, treeHeight);
        }

        minTreeHeight = Integer.MAX_VALUE;
        treeHeight = 0;
        return minHeightTrees;
    }

    private static int minTreeHeight = Integer.MAX_VALUE;
    private static int treeHeight = 0;

    private void getTreeHeight(int start, Map<Integer, List<Integer>> map, boolean[] visit, int height) {
        treeHeight = Math.max(treeHeight, height);
        if (treeHeight > minTreeHeight) return;
        if (!map.containsKey(start)) return;
        for (int end : map.get(start)) {
            if (!visit[end]) {
                visit[end] = true;
                getTreeHeight(end, map, visit, height + 1);
            }
        }
    }
}
