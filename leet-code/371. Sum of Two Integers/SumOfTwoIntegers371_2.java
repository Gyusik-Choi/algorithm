package com.example;

public class SumOfTwoIntegers371_2 {
    public int getSum(int a, int b) {
        while (b != 0) {
            // 자리올림 계산
            int carry = (a & b) << 1;
            // 자리합 계산 (carry 값을 고려하지 않음)
            a = a ^ b;
            // 자리올림을 b 에 할당
            b = carry;
        }
        return a;
    }
}
