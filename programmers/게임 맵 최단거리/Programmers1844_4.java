package com.example;

import java.util.LinkedList;
import java.util.Queue;

public class Programmers1844_4 {
    private static final int[] yValue = new int[]{-1, 0, 1, 0};
    private static final int[] xValue = new int[]{0, 1, 0, -1};

    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        // y, x, stop
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0, 1});
        maps[0][0] = 0;
        while (!queue.isEmpty()) {
            int[] node = queue.poll();
            // 4방향 탐색
            for (int i = 0; i < 4; i++) {
                int y = yValue[i] + node[0];
                int x = xValue[i] + node[1];
                // 도착
                if (y == n - 1 && x == m - 1) {
                    return node[2] + 1;
                }
                if (0 > y || y >= n || 0 > x || x >= m || maps[y][x] == 0) {
                    continue;
                }
                // 방문 처리
                maps[y][x] = 0;
                queue.add(new int[]{y, x, node[2] + 1});
            }
        }
        return -1;
    }
}
