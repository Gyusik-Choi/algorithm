package com.example.algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B_14888_2 {
    private static int maxNum = Integer.MIN_VALUE;

    private static int minNum = Integer.MAX_VALUE;

    private static int N;

    private static int[] nums;

    private static int[] operators;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        nums = new int[N];
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        operators = new int[4];
        for (int i = 0; i < 4; i++) {
            operators[i] = Integer.parseInt(st2.nextToken());
        }
        dfs(1, nums[0]);
        System.out.println(maxNum);
        System.out.println(minNum);
    }

    private static void dfs(int cur, int sums) {
        if (cur == N) {
            maxNum = Math.max(maxNum, sums);
            minNum = Math.min(minNum, sums);
            return;
        }

        if (operators[0] > 0) {
            operators[0]--;
            dfs(cur + 1, sums + nums[cur]);
            operators[0]++;
        }

        if (operators[1] > 0) {
            operators[1]--;
            dfs(cur + 1, sums - nums[cur]);
            operators[1]++;
        }

        if (operators[2] > 0) {
            operators[2]--;
            dfs(cur + 1, sums * nums[cur]);
            operators[2]++;
        }

        if (operators[3] > 0) {
            operators[3]--;
            if (sums < 0) {
                dfs(cur + 1, sums * -1 / nums[cur] * -1);
            } else if (sums == 0) {
                dfs(cur + 1, 0);
            } else {
                dfs(cur + 1, sums / nums[cur]);
            }
            operators[3]++;
        }
    }
}
