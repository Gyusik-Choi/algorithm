package com.example;

import java.util.Arrays;

public class ValidAnagram242_2 {
    public boolean isAnagram(String s, String t) {
        return isSame(s, t);
    }

    private boolean isSame(String s, String t) {
        char[] sCharArray = s.toCharArray();
        Arrays.sort(sCharArray);
        char[] tCharArray = t.toCharArray();
        Arrays.sort(tCharArray);
        return Arrays.toString(sCharArray).equals(Arrays.toString(tCharArray));
    }
}
