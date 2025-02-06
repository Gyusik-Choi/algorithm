package com.example;

public class Programmers92335 {

    public int solution(int n, int k) {
        String kNumber = convertNumber(n, k);
        String[] numbers = kNumber.split("0");

        int primeNumberCount = 0;
        for (String number : numbers) {
            // "110011" 을 "0" 으로 split 하면
            // ["11", "", "11"] 이 된다
            if (number.isEmpty()) continue;
            if (isPrimeNumber(Long.parseLong(number))) primeNumberCount += 1;
        }
        return primeNumberCount;
    }

    private String convertNumber(int n, int k) {
        StringBuilder kNumber = new StringBuilder();
        while (n > 0) {
            kNumber.append(n % k);
            n /= k;
        }
        return kNumber.reverse().toString();
    }

    private boolean isPrimeNumber(long number) {
        if (number < 2) return false;
        for (int i = 3; i <= (int) Math.sqrt(number); i++)
            if (number % i == 0) return false;
        return true;
    }
}
