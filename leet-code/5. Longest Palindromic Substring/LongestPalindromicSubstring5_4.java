package com.example;

public class LongestPalindromicSubstring5_4 {
    private String palindrome = "";

    public String longestPalindrome(String s) {
        for (int i = 0; i < s.length(); i++) {
            findPalindrome(s, i, i);
            findPalindrome(s, i, i + 1);
        }
        return palindrome;
    }

    private void findPalindrome(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            if (palindrome.length() <= right - left + 1) {
                palindrome = s.substring(left, right + 1);
            }
            left--;
            right++;
        }
    }
}
