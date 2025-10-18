package com.example;

import java.util.ArrayDeque;
import java.util.Queue;

public class Programmers1844_3 {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        int[] yValue = new int[]{-1, 0, 1, 0};
        int[] xValue = new int[]{0, 1, 0, -1};
        // y축, x축, 거리
        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{0, 0, 1});
        while (!queue.isEmpty()) {
            int[] path = queue.poll();
            if (path[0] == n - 1 && path[1] == m - 1) {
                return path[2];
            }
            for (int i = 0; i < 4; i++) {
                int y = path[0] + yValue[i];
                int x = path[1] + xValue[i];
                if (0 > y || y >= n || 0 > x || x >= m || maps[y][x] == 0) {
                    continue;
                }
                maps[y][x] = 0;
                queue.offer(new int[]{y, x, path[2] + 1});
            }
        }
        return -1;
    }
}
