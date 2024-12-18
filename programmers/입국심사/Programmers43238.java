package com.example;

import java.util.Arrays;

public class Programmers43238 {
    public long solution(int n, int[] times) {
        long left = 1;
        long right = (long) Arrays.stream(times).max().getAsInt() * n;
        while (left < right) {
            long mid = left + (right - left) / 2;
            long immigrations = 0;
            for (int time : times) immigrations += mid / time;
            if (immigrations < n) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}
