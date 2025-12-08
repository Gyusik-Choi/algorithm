package com.example;

public class SumOfTwoIntegers371_4 {
    public int getSum(int a, int b) {
        String binA = String.format("%32s", Integer.toBinaryString(a)).replace(' ', '0');
        String binB = String.format("%32s", Integer.toBinaryString(b)).replace(' ', '0');
        StringBuilder sb = new StringBuilder();
        int carryIn = 0;
        for (int i = 31; i >= 0; i--) {
            int A = Character.getNumericValue(binA.charAt(i));
            int B = Character.getNumericValue(binB.charAt(i));
            int sum = (A ^ B) ^ carryIn;
            carryIn = ((A ^ B) & carryIn) | (A & B);
            sb.insert(0, sum);
        }
        return Integer.parseUnsignedInt(sb.toString(), 2);
    }
}
