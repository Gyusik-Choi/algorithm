package com.example;

import java.util.HashMap;
import java.util.Map;

public class FibonacciNumber509 {

    private Map<Integer, Integer> map = new HashMap<>();

    public int fib(int n) {
        if (n <= 1) return n;
        if (map.containsKey(n)) return map.get(n);
        int value = fib(n - 1) + fib(n - 2);
        map.put(n, value);
        return value;
    }
}
