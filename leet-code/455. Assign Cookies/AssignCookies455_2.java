package com.example.algorithm;

import java.util.Arrays;

public class AssignCookies455_2 {

    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int child = 0, cookie = 0;
        while (child < g.length && cookie < s.length) {
            if (g[child] <= s[cookie]) child++;
            cookie++;
        }
        return child;
    }
}
