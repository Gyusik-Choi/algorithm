package com.example;

public class DisjointSet {
    private final int[] path;
    private final int[] height;

    public DisjointSet(int size) {
        path = new int[size];
        height = new int[size];

        for (int i = 1; i < size; i++) {
            path[i] = i;
        }
    }

    public int findSet(int a) {
        if (path[a] != a) {
            path[a] = findSet(path[a]);
        }
        return path[a];
    }

    public void unionSet(int a, int b) {
        int px = findSet(a);
        int py = findSet(b);

        if (height[px] >= height[py]) {
            path[py] = px;
            if (height[px] == height[py]) {
                height[px] += 1;
            }
        } else {
            path[px] = py;
        }
    }
}
