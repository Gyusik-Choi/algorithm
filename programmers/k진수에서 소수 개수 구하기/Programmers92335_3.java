package com.example;

import java.util.Arrays;

public class Programmers92335_3 {
    // 1 ≤ n ≤ 1,000,000
    // 3 ≤ k ≤ 10
    public int solution(int n, int k) {
        String kDigit = convertToKDigit(n, k);
        String[] digits = kDigit.replace("0", " ").split("\\s+");
        return (int) Arrays.stream(digits)
                .filter(d -> isPrime(Long.parseLong(d)))
                .count();
    }

    private String convertToKDigit(int n, int k) {
        StringBuilder sb = new StringBuilder();
        while (n > 0) {
            sb.insert(0, n % k);
            n /= k;
        }
        return sb.toString();
    }

    private boolean isPrime(long num) {
        if (num < 2) return false;
        int sqrt = (int) Math.sqrt(num);
        for (int n = 2; n <= sqrt; n++) {
            if (num % n == 0) {
                return false;
            }
        }
        return true;
    }
}
