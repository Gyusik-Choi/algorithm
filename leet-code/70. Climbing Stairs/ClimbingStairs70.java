package com.example.algorithm;

import java.util.HashMap;
import java.util.Map;

public class ClimbingStairs70 {

    private Map<Integer, Integer> memo = new HashMap<>();

    public int climbStairs(int n) {
        if (n <= 2) return n;
        if (memo.containsKey(n)) return memo.get(n);
        int res = climbStairs(n - 1) + climbStairs(n - 2);
        memo.put(n, res);
        return res;
    }
}
