package com.example;

public class ValidPalindrome125_6 {
    public boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            char leftChar = s.charAt(left);
            char rightChar = s.charAt(right);
            if (!Character.isLetterOrDigit(leftChar)) {
                left += 1;
            } else if (!Character.isLetterOrDigit(rightChar)) {
                right -= 1;
            } else {
                if (Character.toLowerCase(leftChar) != Character.toLowerCase(rightChar)) {
                    return false;
                }
                left += 1;
                right -= 1;
            }
        }
        return true;
    }
}
