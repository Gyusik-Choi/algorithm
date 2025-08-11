package com.example;

public class ValidPalindrome125_5 {
    public boolean isPalindrome(String s) {
        String filteredWord = s.replaceAll("[^0-9a-zA-Z]", "").toLowerCase();
        return filteredWord.equals(reverse(filteredWord));
    }

    private String reverse(String s) {
        String str = "";
        for (int i = 0; i < s.length(); i++) {
            str = String.valueOf(s.charAt(i)).concat(str);
        }
        return str;
    }
}
