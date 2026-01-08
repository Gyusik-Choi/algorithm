package com.example;

public class ClimbingStairs70_2 {
    public int climbStairs(int n) {
        // 1 <= n <= 45
        // 피보나치와 유사하다
        // n 이 현재 위치라면 n - 2 or n - 1 에서 왔다
        if (n < 3) {
            return n;
        }
        int[] arr = new int[n + 1];
        arr[1] = 1;
        arr[2] = 2;
        for (int i = 3; i <= n; i++) {
            arr[i] = arr[i - 1] + arr[i - 2];
        }
        return arr[n];
    }
}
