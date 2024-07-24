public class LongestPalindromeSubstring5_2 {
    int start = 0;
    int maxLength = 0;

    public String longestPalindrome(String s) {
        if (s.length() == 1) {
            return s;
        }

        for (int i = 0; i < s.length() - 1; i++) {
            findPalindrome(i, i + 1, s);
            findPalindrome(i, i + 2, s);
        }

        return s.substring(start, start + maxLength);
    }

    private void findPalindrome(int left, int right, String s) {
        while (left >= 0 && right <= s.length() - 1 && s.charAt(left) == s.charAt(right)) {
            left -= 1;
            right += 1;
        }

        if (maxLength < right - left - 1) {
            start = left + 1;
            maxLength = right - left - 1;
        }
    }
}
