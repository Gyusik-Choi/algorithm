package com.example;

import java.util.Arrays;

public class Programmers42897_3 {
    public int solution(int[] money) {
        // [2, 1, 1, 3]
        // -> [2, 2, 3] / [1, 1, 4]
        int[] moneyWithoutLast = Arrays.copyOfRange(money, 0, money.length - 1);
        moneyWithoutLast[1] = Math.max(moneyWithoutLast[0], moneyWithoutLast[1]);
        for (int i = 2; i < money.length - 1; i++) {
            moneyWithoutLast[i] = Math.max(moneyWithoutLast[i - 2] + moneyWithoutLast[i], moneyWithoutLast[i - 1]);
        }
        int[] moneyWithoutFirst = Arrays.copyOfRange(money, 1, money.length);
        moneyWithoutFirst[1] = Math.max(moneyWithoutFirst[0], moneyWithoutFirst[1]);
        for (int i = 2; i < money.length - 1; i++) {
            moneyWithoutFirst[i] = Math.max(moneyWithoutFirst[i - 2] + moneyWithoutFirst[i], moneyWithoutFirst[i - 1]);
        }
        return Math.max(moneyWithoutLast[money.length - 2], moneyWithoutFirst[money.length - 2]);
    }
}
