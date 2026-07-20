package com.example;

public class NumberOf1Bits191_5 {
    public int hammingWeight(int n) {
        int count = 0;
        while (n > 0) {
            n &= (n - 1);
            count++;
        }
        return count;
    }
}
