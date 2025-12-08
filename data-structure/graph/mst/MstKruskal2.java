package com.example;

import java.util.*;

public class MstKruskal2 {
    /**
     * mst prim 과 달리 간선을 중심으로 진행하기 때문에
     * 탐색을 시작하기 전에 모든 노드를 우선순위 큐에 넣어서
     * 최소 비용이 드는 간선을 선택할 수 있도록 한다
     */
    public int kruskal(int n, int[][] data) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[2]));
        for (int[] path : data) {
            pq.add(path);
        }
        DisjointSet set = new DisjointSet(n);
        int total = 0;

        while (!pq.isEmpty()) {
            int[] node = pq.poll();
            int px = set.findSet(node[0]);
            int py = set.findSet(node[1]);

            if (px == py) {
                continue;
            }

            total += node[2];
            set.unionSet(node[0], node[1]);
        }
        return total;
    }

    static class DisjointSet {
        private final int size;
        private final int[] parent;
        private final int[] height;

        DisjointSet(int size) {
            this.size = size;
            this.parent = new int[size + 1];
            this.height = new int[size + 1];
            for (int i = 1; i < size; i++) {
                parent[i] = i;
            }
        }

        public int findSet(int x) {
            if (parent[x] != x) {
                parent[x] = findSet(parent[x]);
            }
            return parent[x];
        }

        public void unionSet(int x, int y) {
            int px = findSet(x);
            int py = findSet(y);

            if (height[px] >= height[py]) {
                parent[py] = px;
                if (height[px] == height[py]) {
                    height[px] += 1;
                }
            } else {
                parent[px] = py;
            }
        }
    }
}
