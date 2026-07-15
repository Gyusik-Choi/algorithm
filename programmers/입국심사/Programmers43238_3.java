package com.example;

public class Programmers43238_3 {
    public long solution(int n, int[] times) {
        long left = 0, right = (long) getMaxTime(times) * n / times.length;
        while (left < right) {
            long mid = left + (right - left) / 2;
            long totalImmigrationNumber = getTotalImmigrationNumber(times, mid);
            if (n <= totalImmigrationNumber) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    private int getMaxTime(int[] times) {
        int maxTime = times[0];
        for (int i = 1; i < times.length; i++) {
            if (times[i] > maxTime) {
                maxTime = times[i];
            }
        }
        return maxTime;
    }

    private long getTotalImmigrationNumber(int[] times, long time) {
        long immigrationNumber = 0;
        for (int i : times) {
            immigrationNumber += time / i;
        }
        return immigrationNumber;
    }
}
