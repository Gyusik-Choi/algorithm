package com.example;

public class FibonacciNumber509_4 {
    private final int[] arr = new int[31];

    public int fib(int n) {
        if (n == 0 || n == 1) {
            return n;
        }
        if (arr[n] > 0) {
            return arr[n];
        }
        arr[n] = fib(n - 1) + fib(n - 2);
        return arr[n];
    }
}
