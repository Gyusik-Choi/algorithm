package com.example;

import java.util.Arrays;

public class AssignCookies455_3 {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int count = 0;
        int gIdx = 0;
        for (int size : s) {
            if (gIdx == g.length) break;
            if (size < g[gIdx]) continue;
            gIdx += 1;
            count += 1;
        }
        return count;
    }
}
