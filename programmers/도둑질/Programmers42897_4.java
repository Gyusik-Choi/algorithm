package com.example;

import java.util.Arrays;

public class Programmers42897_4 {
    public int solution(int[] money) {
        int[] dp1 = getDpArray(Arrays.copyOfRange(money, 0, money.length - 1));
        int[] dp2 = getDpArray(Arrays.copyOfRange(money, 1, money.length));
        return Math.max(dp1[dp1.length - 1], dp2[dp2.length - 1]);
    }

    private int[] getDpArray(int[] arr) {
        int[] dp = new int[arr.length];
        dp[0] = arr[0];
        dp[1] = Math.max(dp[0], arr[1]);
        for (int i = 2; i < dp.length; i++) dp[i] = Math.max(dp[i - 2] + arr[i], dp[i - 1]);
        return dp;
    }
}
