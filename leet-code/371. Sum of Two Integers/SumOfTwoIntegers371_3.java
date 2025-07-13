package com.example;

public class SumOfTwoIntegers371_3 {
    public int getSum(int a, int b) {
        String binaryA = String.format("%32s", Integer.toBinaryString(a)).replaceAll(" ", "0");
        String binaryB = String.format("%32s", Integer.toBinaryString(b)).replaceAll(" ", "0");
        int integerLength = 32;
        int sum = 0;
        int carry = 0;
        StringBuilder answer = new StringBuilder();
        for (int i = integerLength - 1; i > -1; i--) {
            int bitA = Character.getNumericValue(binaryA.charAt(i));
            int bitB = Character.getNumericValue(binaryB.charAt(i));
            sum = (bitA ^ bitB) ^ carry;
            carry = (((bitA ^ bitB) & carry) | (bitA & bitB));
            answer.insert(0, sum);
        }
        return Integer.parseUnsignedInt(answer.toString(), 2);
    }
}
