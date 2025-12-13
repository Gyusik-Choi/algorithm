package com.example;

public class UTF8Validation393_2 {
    public boolean validUtf8(int[] data) {
        int idx = 0;
        while (idx < data.length) {
            int num = data[idx];
            int firstBitCount = getFirstBitCount(num);
            if (firstBitCount == 1 || firstBitCount > 4 || (firstBitCount > 0 && idx + firstBitCount > data.length)) {
                return false;
            }
            for (int i = idx + 1; i < idx + firstBitCount; i++) {
                int bitCount = getFirstBitCount(data[i]);
                if (bitCount != 1) {
                    return false;
                }
            }
            if (firstBitCount == 0) {
                idx += 1;
            } else {
                idx += firstBitCount;
            }
        }
        return true;
    }

    private int getFirstBitCount(int num) {
        // 8자리 2진수로 만들어서 확인해야 한다
        String binary = String.format("%8s", Integer.toBinaryString(num))
                .replace(" ", "0");
        int count = 0;
        for (char b : binary.toCharArray()) {
            if (b == '1') {
                count += 1;
            } else {
                break;
            }
        }
        return count;
    }
}
