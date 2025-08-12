package com.example;

import java.util.Arrays;

public class ReverseString344_2 {
    public void reverseString(char[] s) {
        int sLength = s.length;
        int mid = (sLength - 1) / 2;
        for (int i = 0; i <= mid; i++) {
            System.out.println("s[i], s[sLength() - i - 1] = " + s[i] + " " + s[sLength - i - 1]);
            char left = s[i];
            s[i] = s[sLength - 1 - i];
            s[sLength - 1 - i] = left;
        }
        System.out.println(Arrays.toString(s));
    }
}
