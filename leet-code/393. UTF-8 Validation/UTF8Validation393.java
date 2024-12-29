package com.example;

public class UTF8Validation393 {
    // data 를 while 문을 돌면서
    // 해당 인덱스의 숫자가 몇바이트가 필요한지 판단하고
    // 해당 인덱스의 최상위 바이트 형태가 올바른지 판단하고
    // 나머지 바이트들의 최상위 2비트 형태가 10 인지 판단한다
    public boolean validUtf8(int[] data) {
        int idx = 0;
        while (idx < data.length) {
            if (data[idx] >> 3 == 0b11110) {
                if (!isValidUtf8(data, idx + 1, 3)) return false;
                idx += 4;
            } else if (data[idx] >> 4 == 0b1110) {
                if (!isValidUtf8(data, idx + 1, 2)) return false;
                idx += 3;
            } else if (data[idx] >> 5 == 0b110) {
                if (!isValidUtf8(data, idx + 1, 1)) return false;
                idx += 2;
            } else if (data[idx] >> 7 == 0b0) {
                idx += 1;
            } else {
                return false;
            }
        }
        return true;
    }

    private boolean isValidUtf8(int[] data, int start, int length) {
        for (int i = start; i < start + length; i++)
            if (i >= data.length || data[i] >> 6 != 0b10) return false;
        return true;
    }
}
