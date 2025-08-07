package com.example;

public class Programmers42897_2 {
    public int solution(int[] money) {
        if (money.length == 1) {
            return money[0];
        }
        if (money.length == 2) {
            return Math.max(money[0], money[1]);
        }
        if (money.length == 3) {
            return Math.max(Math.max(money[0], money[1]), money[2]);
        }

        // 길이 4부터 dp 배열 사용
        int[] dp1 = new int[money.length];
        int[] dp2 = new int[money.length];
        dp1[0] = money[0];
        dp1[1] = Math.max(dp1[0], money[1]);
        dp2[1] = money[1];
        for (int i = 2; i < money.length; i++) {
            dp1[i] = Math.max(dp1[i - 2] + money[i], dp1[i - 1]);
            dp2[i] = Math.max(dp2[i - 2] + money[i], dp2[i - 1]);
        }
        return Math.max(dp1[money.length - 2], dp2[money.length - 1]);
    }
}
