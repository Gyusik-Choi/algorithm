package com.example;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B_1912 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) arr[i] = Integer.parseInt(st.nextToken());

        int[] dp = new int[n];
        dp[0] = arr[0];
        if (n > 1) for (int i = 1; i < n; i++) dp[i] = Math.max(dp[i - 1] + arr[i], arr[i]);
        System.out.println(Arrays.stream(dp).max().getAsInt());
    }
}
