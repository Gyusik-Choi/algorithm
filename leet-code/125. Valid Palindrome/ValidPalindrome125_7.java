package com.example;

public class ValidPalindrome125_7 {
    public boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            while (left < right && isNotAlphaNumeric(s.charAt(left))) left++;
            while (left < right && isNotAlphaNumeric(s.charAt(right))) right--;
            if (!String.valueOf(s.charAt(left)).equalsIgnoreCase(String.valueOf(s.charAt(right)))) return false;
            left++;
            right--;
        }
        return true;
    }

    private boolean isNotAlphaNumeric(char c) {
//        return String.valueOf(c).matches("[^0-9a-zA-Z]");
        return !Character.isLetterOrDigit(c);
    }
}
