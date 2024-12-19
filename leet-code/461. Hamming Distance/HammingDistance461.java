package com.example;

public class HammingDistance461 {

    public int hammingDistance(int x, int y) {
        System.out.println(Integer.bitCount(x));
        return Integer.bitCount(x ^ y);
    }
}
