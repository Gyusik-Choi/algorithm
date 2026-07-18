package com.example;

public class UTF8Validation393_3 {
    public boolean validUtf8(int[] data) {
        // 0 -> 7비트
        // 110 10 -> 8~11비트
        // 1110 10 10 -> 12~16비트
        // 11110 10 10 10 -> 17비트~21비트
        int idx = 0;
        while (idx < data.length) {
            String binary = convertIntoBinary(data[idx]);
            if (binary.startsWith("11111")) {
                return false;
            }
            if (binary.startsWith("11110")) {
                if (idx + 3 >= data.length) {
                    return false;
                }
                for (int i = idx + 1; i <= idx + 3; i++) {
                    if (!convertIntoBinary(data[i]).startsWith("10")) {
                        return false;
                    }
                }
                idx += 4;
                continue;
            }
            if (binary.startsWith("1110")) {
                if (idx + 2 >= data.length) {
                    return false;
                }
                for (int i = idx + 1; i <= idx + 2; i++) {
                    if (!convertIntoBinary(data[i]).startsWith("10")) {
                        return false;
                    }
                }
                idx += 3;
                continue;
            }
            if (binary.startsWith("110")) {
                if (idx + 1 >= data.length) {
                    return false;
                }
                for (int i = idx + 1; i <= idx + 1; i++) {
                    if (!convertIntoBinary(data[i]).startsWith("10")) {
                        return false;
                    }
                }
                idx += 2;
                continue;
            }
            if (binary.startsWith("10")) {
                return false;
            }
            idx += 1;
        }
        return true;
    }

    private String convertIntoBinary(int num) {
        StringBuilder sb = new StringBuilder();
        while (num > 0) {
            sb.insert(0, num % 2);
            num /= 2;
        }
        return String.format("%8s", sb).replace(' ', '0');
    }
}
