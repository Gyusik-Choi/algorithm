public class LongestPalindromeSubstring5_3 {
    public String longestPalindrome(String s) {
        if (s.length() == 1) {
            return s;
        }

        int start = 0;
        int maxLength = 0;

        for (int i = 0; i < s.length() - 1; i++) {
            int[] evenIdx = findPalindrome(i, i + 1, s);
            int[] oddIdx = findPalindrome(i, i + 2, s);

            if (evenIdx[1] - evenIdx[0] - 1 > maxLength) {
                start = evenIdx[0] + 1;
                maxLength = evenIdx[1] - evenIdx[0] - 1;
            }
            if (oddIdx[1] - oddIdx[0] - 1 > maxLength) {
                start = oddIdx[0] + 1;
                maxLength = oddIdx[1] - oddIdx[0] - 1;
            }
        }

        return s.substring(start, start + maxLength);
    }

    private int[] findPalindrome(int left, int right, String s) {
        while (left >= 0 && right <= s.length() - 1 && s.charAt(left) == s.charAt(right)) {
            left -= 1;
            right += 1;
        }
        return new int[]{left, right};
    }
}
