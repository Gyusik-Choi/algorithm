package com.example;

import java.util.LinkedList;
import java.util.Queue;

public class Programmers1844_2 {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        int[] yValue = new int[]{-1, 0, 1, 0};
        int[] xValue = new int[]{0, 1, 0, -1};

        Queue<Node> q = new LinkedList<>();
        q.add(new Node(0, 0, 1));
        maps[0][0] = 0;

        while (!q.isEmpty()) {
            Node start = q.poll();

            for (int i = 0; i < 4; i++) {
                int y = start.y + yValue[i];
                int x = start.x + xValue[i];

                if (0 > y || y >= n || 0 > x || x >= m) {
                    continue;
                }

                if (maps[y][x] == 0) {
                    continue;
                }

                if (y == n - 1 && x == m - 1) {
                    return start.step + 1;
                }

                maps[y][x] = 0;
                q.add(new Node(y, x, start.step + 1));
            }
        }

        return -1;
    }

    private static class Node {
        int y;
        int x;
        int step;

        Node(int y, int x, int step) {
            this.y = y;
            this.x = x;
            this.step = step;
        }
    }
}
