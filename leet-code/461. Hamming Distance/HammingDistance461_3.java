package com.example;

public class HammingDistance461_3 {
    public int hammingDistance(int x, int y) {
        // xor 연산 후에 1을 카운트
        return Integer.bitCount(x ^ y);
    }
}
