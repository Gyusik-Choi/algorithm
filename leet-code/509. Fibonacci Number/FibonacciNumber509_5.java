package com.example;

import java.util.HashMap;
import java.util.Map;

public class FibonacciNumber509_5 {
    private final Map<Integer, Integer> memo = new HashMap<>(Map.of(0, 0, 1, 1));

    public int fib(int n) {
        if (memo.containsKey(n)) return memo.get(n);
        memo.put(n, fib(n - 1) + fib(n - 2));
        return memo.get(n);
    }
}
