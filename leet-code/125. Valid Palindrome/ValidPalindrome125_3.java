package com.example;

public class ValidPalindrome125_3 {
    public boolean isPalindrome(String s) {
        StringBuilder sb = new StringBuilder().append(s
                .replaceAll("[^a-zA-Z0-9]", "")
                .toLowerCase());
        return sb.toString().contentEquals(sb.reverse());
    }
}
