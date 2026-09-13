package com.example;

public class LongestPalindromicSubstring5_5 {
    public String longestPalindrome(String s) {
        String palindrome = "";
        for (int i = 0; i < s.length(); i++) {
            String oddPalindrome = getPalindrome(s, i, i);
            if (palindrome.length() < oddPalindrome.length()) palindrome = oddPalindrome;
            String evenPalindrome = getPalindrome(s, i, i + 1);
            if (palindrome.length() < evenPalindrome.length()) palindrome = evenPalindrome;
        }
        return palindrome;
    }

    private String getPalindrome(String s, int left, int right) {
        if (right >= s.length() || s.charAt(left) != s.charAt(right)) return "";
        while (0 <= left && right <= s.length() - 1 && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        // 조건을 만족하면 left 은 1 감소, right 는 1 증가된 상태에서 while 문이 종료되기 때문에
        // left 는 1 증가, right 는 1 감소시켜야 실제 팰린드롬 길이로 보정된다
        return s.substring(left + 1, right);
    }
}
