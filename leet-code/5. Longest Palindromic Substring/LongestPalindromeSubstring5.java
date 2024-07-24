public class LongestPalindromeSubstring5 {
    public String longestPalindrome(String s) {
        if (s.length() == 1) {
            return s;
        }

        // s 가 "ac" 일때 주어지면
        // 리턴값이 "" 이 아니라 "a" 혹은 "c"가 돼야해서
        // palindrome 의 초기값으로 s 의 첫번째 글자를 설정함
        String palindrome = s.substring(0, 1);
        for (int i = 0; i < s.length(); i++) {
            String even = findPalindrome(i, i + 1, s);
            String odd = findPalindrome(i - 1, i + 1, s);
            if (palindrome.length() < even.length()) {
                palindrome = even;
            }
            if (palindrome.length() < odd.length()) {
                palindrome = odd;
            }
        }
        return palindrome;
    }

    private String findPalindrome(int left, int right, String s) {
        String palindrome = "";
        while (left >= 0 && right <= s.length() - 1 && s.charAt(left) == s.charAt(right)) {
            palindrome = s.substring(left, right + 1);
            left -= 1;
            right += 1;
        }
        return palindrome;
    }
}
