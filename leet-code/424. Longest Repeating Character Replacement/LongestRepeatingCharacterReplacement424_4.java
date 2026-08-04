package com.example;

public class LongestRepeatingCharacterReplacement424_4 {
    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int maxCount = 0;
        int maxLength = 0;
        int left = 0;
        for (int right = 0; right < s.length(); right++) {
            int rightIdx = s.charAt(right) - 'A';
            count[rightIdx]++;
            maxCount = Math.max(maxCount, count[rightIdx]);
            if (right - left + 1 <= maxCount + k) {
                maxLength = Math.max(maxLength, right - left + 1);
            } else {
                int leftIdx = s.charAt(left) - 'A';
                count[leftIdx]--;
                left += 1;
            }
        }
        return maxLength;
    }
}
