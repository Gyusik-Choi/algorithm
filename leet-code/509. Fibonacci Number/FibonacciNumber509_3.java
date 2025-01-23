package com.example;

public class FibonacciNumber509_3 {

    public int fib(int n) {
        // 0 1
        // 1 1
        // 1 2
        // 2 3
        // 3 5
        // 5 8
        int x = 0, y = 1;
        for (int i = 0; i < n; i++) {
            int z = x + y;
            x = y;
            y = z;
        }
        return x;
    }
}
