package com.example;

public class HammingDistance461_2 {
    public int hammingDistance(int x, int y) {
        return countOneBit(toBinary(x ^ y));
    }

    private String toBinary(int num) {
        StringBuilder sb = new StringBuilder();
        while (num > 0) {
            sb.insert(0, num % 2);
            num /= 2;
        }
        return sb.toString();
    }

    private int countOneBit(String binary) {
        int count = 0;
        for (char b : binary.toCharArray()) {
            if (b == '1') {
                count += 1;
            }
        }
        return count;
    }
}
