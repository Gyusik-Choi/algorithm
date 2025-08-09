package com.example.algorithm;

import java.util.Arrays;

public class Programmers92335_2 {
    public int solution(int n, int k) {
        String kNumber = toKNumber(n, k);
        String[] strNumbers = kNumber.split("0");
        return (int) Arrays.stream(strNumbers)
                .filter(s -> !s.isEmpty() && isPrimeNumber(Long.parseLong(s)))
                .count();
    }

    private String toKNumber(int n, int k) {
        StringBuilder sb = new StringBuilder();
        while (n > 0) {
            sb.insert(0, n % k);
            n /= k;
        }
        return sb.toString();
    }

    private Boolean isPrimeNumber(long n) {
        int sqrt = (int) Math.sqrt(n);
        if (n == 1) {
            return false;
        }
        for (int i = 2; i <= sqrt; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
