package com.example.algorithm;

import java.util.Arrays;

public class AssignCookies455 {

    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int answer = 0, child = 0, cookie = 0;
        while (child < g.length && cookie < s.length) {
            if (g[child] <= s[cookie]) {
                answer++;
                child++;
            }
            cookie++;
        }
        return answer;
    }
}
